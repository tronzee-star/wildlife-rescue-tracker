from datetime import date
from tabulate import tabulate
from app.database import SessionLocal
from app.models import Location, RescueCenter, Animal


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


# -------- Main Menu --------
def main():
    MENU = """
Wildlife Rescue Tracker

1) Add Animal
2) List Animals
3) Add Location
4) List Locations
5) Add Rescue Center
6) List Rescue Centers
7) Exit
"""
    while True:
        choice = input(MENU).strip()
        if choice == "1":
            add_animal()
        elif choice == "2":
            list_animals()
        elif choice == "3":
            add_location()
        elif choice == "4":
            list_locations()
        elif choice == "5":
            add_rescue_center()
        elif choice == "6":
            list_rescue_centers()
        elif choice == "7":
            print("Goodbye 👋")
            break
        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    main()
