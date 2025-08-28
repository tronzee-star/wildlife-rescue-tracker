# test_db.py
from app.database import SessionLocal, engine, Base
from app.models import RescueCenter, Animal

# Create tables in the database
Base.metadata.create_all(bind=engine)

# Open a session
session = SessionLocal()

# Create a rescue center
center = RescueCenter(name="Nairobi Wildlife Rescue", location="Nairobi")
session.add(center)
session.commit()
session.refresh(center)

# Add animals to that rescue center
lion = Animal(species="Lion", name="Simba", rescue_center_id=center.id)
elephant = Animal(species="Elephant", name="Tembo", rescue_center_id=center.id)

session.add_all([lion, elephant])
session.commit()

# Query the database
centers = session.query(RescueCenter).all()
for c in centers:
    print(f"Rescue Center: {c.name} in {c.location}")
    for a in c.animals:
        print(f"  - {a.species} named {a.name}")

session.close()
