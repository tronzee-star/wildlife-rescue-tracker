from datetime import date
from tabulate import tabulate
from app.database import SessionLocal
from app.models import Location, RescueCenter, Animal
from app.reports import (
    list_animals_by_species,
    find_animals_by_region
)

# -------- Animal --------
def add_animal():
    name = input("Animal name: ").strip()
    species = input("Species: ").strip()
    rescue_center_id = int(input("Rescue Center ID: "))
    with SessionLocal() as db:
        db.add(Animal(name=name, species=species, rescue_center_id=rescue_center_id))
        db.commit()
    print("✅ Animal added.")

def list_animals():
    with SessionLocal() as db:
        rows = db.query(Animal).order_by(Animal.name).all()
        table = [(a.id, a.name, a.species, a.rescue_center_id) for a in rows]
        print(tabulate(table, headers=["ID", "Name", "Species", "Rescue Center ID"], tablefmt="github"))

def delete_animal():
    with SessionLocal() as db:
        animals = db.query(Animal).order_by(Animal.id).all()
        if not animals:
            print("❌ No animals found.")
            return

        table = [(a.id, a.name, a.species, a.rescue_center_id) for a in animals]
        print(tabulate(table, headers=["ID", "Name", "Species", "Rescue Center ID"], tablefmt="github"))

        try:
            animal_id = int(input("Enter the ID of the animal to delete: "))
        except ValueError:
            print("❌ Invalid input")
            return

        animal = db.query(Animal).filter(Animal.id == animal_id).first()
        if animal:
            db.delete(animal)
            db.commit()
            print("✅ Animal deleted.")
        else:
            print("❌ Animal not found.")

# -------- Location --------
def add_location():
    name = input("Location name: ").strip()
    region = input("Region: ").strip()
    with SessionLocal() as db:
        db.add(Location(name=name, region=region))
        db.commit()
    print("✅ Location added.")

def list_locations():
    with SessionLocal() as db:
        rows = db.query(Location).order_by(Location.name).all()
        table = [(l.id, l.name, l.region) for l in rows]
        print(tabulate(table, headers=["ID", "Name", "Region"], tablefmt="github"))

# -------- Rescue Center --------
def add_rescue_center():
    name = input("Rescue Center name: ").strip()
    location_id = int(input("Location ID: "))
    with SessionLocal() as db:
        db.add(RescueCenter(name=name, location_id=location_id))
        db.commit()
    print("✅ Rescue Center added.")

def list_rescue_centers():
    with SessionLocal() as db:
        rows = db.query(RescueCenter).order_by(RescueCenter.name).all()
        table = [(rc.id, rc.name, rc.location_id) for rc in rows]
        print(tabulate(table, headers=["ID", "Name", "Location ID"], tablefmt="github"))

# -------- Reports Menu --------
def reports_menu(session):
    while True:
        print("\n📊 Reports Menu")
        print("1. List animals by species")
        print("2. Find animals by region")
        print("0. Back to main menu")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            list_animals_by_species(session)
        elif choice == "2":
            region = input("Enter region name: ")
            find_animals_by_region(session, region)
        elif choice == "0":
            break
        else:
            print("❌ Invalid choice, try again.")

# -------- Main Menu --------
def main():
    MENU = """
Wildlife Rescue Tracker

1) Add Animal
2) List Animals
3) Delete Animal
4) Add Location
5) List Locations
6) Add Rescue Center
7) List Rescue Centers
8) Reports
9) Exit
"""
    with SessionLocal() as session:
        while True:
            choice = input(MENU).strip()
            if choice == "1":
                add_animal()
            elif choice == "2":
                list_animals()
            elif choice == "3":
                delete_animal()
            elif choice == "4":
                add_location()
            elif choice == "5":
                list_locations()
            elif choice == "6":
                add_rescue_center()
            elif choice == "7":
                list_rescue_centers()
            elif choice == "8":
                reports_menu(session)
            elif choice == "9":
                print("Goodbye 👋")
                break
            else:
                print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
