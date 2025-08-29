# wildlife-rescue-tracker
# 🐾 Wildlife Rescue Tracker CLI

The **Wildlife Rescue Tracker** is a Python command-line application that helps track animals, rescue centers, and locations. It allows users to **add, list, delete animals**, manage rescue centers and locations, and generate basic reports.

---

## **Features**

- **Animals**
  - Add new animals with name, species, and rescue center.
  - List all animals in a neatly formatted table.
  - Delete animals by ID.
  
- **Locations**
  - Add new locations with name and region.
  - List all locations.

- **Rescue Centers**
  - Add new rescue centers with name and associated location.
  - List all rescue centers.

- **Reports**
  - List animals by species.
  - Find animals by region.

---

## **Dependencies**

- Python 3.8+
- [SQLAlchemy](https://www.sqlalchemy.org/) – ORM for database management.
- [Tabulate](https://pypi.org/project/tabulate/) – Display tables in CLI.
- [Alembic](https://alembic.sqlalchemy.org/) – Optional for database migrations.

Install dependencies via pip:

```bash
pip install sqlalchemy tabulate alembic
