

from app.database import engine, Base
from app import models
from app.cli import run_cli


def init_db():
    Base.metadata.create_all(bind=engine)
    print("✅ Database initialized successfully!")


if __name__ == "__main__":
    init_db()
    run_cli()

    from app.database import engine, Base
from app import models

# Create all tables defined in models.py
Base.metadata.create_all(bind=engine)

print("✅ Tables created successfully!")

