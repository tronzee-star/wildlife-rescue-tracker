from sqlalchemy.orm import Session
from app.models import Animal, RescueCenter, Location

# ----- Animal Reports -----
def list_animals_by_species(session: Session):
    results = session.query(Animal.species, Animal.name).all()
    print("\n🐾 Animals by Species:")
    for species, name in results:
        print(f" - {name} ({species})")

def count_animals_per_center(session: Session):
    results = (
        session.query(RescueCenter.name, func.count(Animal.id))
        .join(Animal, RescueCenter.animals)
        .group_by(RescueCenter.id)
        .all()
    )
    print("\n🏥 Animals per Rescue Center:")
    for center, count in results:
        print(f" - {center}: {count} animals")

# ----- Location Reports -----
def count_centers_per_location(session: Session):
    results = (
        session.query(Location.name, func.count(RescueCenter.id))
        .join(RescueCenter, Location.rescue_centers)
        .group_by(Location.id)
        .all()
    )
    print("\n🌍 Rescue Centers per Location:")
    for location, count in results:
        print(f" - {location}: {count} centers")

def find_animals_by_region(session: Session, region: str):
    results = (
        session.query(Animal.name, Animal.species, Location.region)
        .join(RescueCenter, Animal.rescue_center)
        .join(Location, RescueCenter.location)
        .filter(Location.region == region)
        .all()
    )
    print(f"\n🔎 Animals in region: {region}")
    for name, species, _ in results:
        print(f" - {name} ({species})")
