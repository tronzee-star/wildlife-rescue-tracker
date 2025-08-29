import sqlite3

conn = sqlite3.connect("wildlife.db")
cursor = conn.cursor()

# List all tables
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()
print("Tables in database:", tables)

# Fetch all animals
cursor.execute("SELECT * FROM animals;")  # lowercase 'animals'
animals = cursor.fetchall()
print("\nAnimals:")
for animal in animals:
    print(animal)

# Fetch all locations
cursor.execute("SELECT * FROM locations;")
locations = cursor.fetchall()
print("\nLocations:")
for loc in locations:
    print(loc)

# Fetch all rescue centers
cursor.execute("SELECT * FROM rescue_centers;")
centers = cursor.fetchall()
print("\nRescue Centers:")
for center in centers:
    print(center)

conn.close()
