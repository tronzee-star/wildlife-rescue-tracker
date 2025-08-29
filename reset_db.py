# reset_db.py
from app.database import Base, engine

print("⚠️  Dropping all tables...")
Base.metadata.drop_all(bind=engine)

print("✅ Recreating tables...")
Base.metadata.create_all(bind=engine)

print("🎉 Database reset complete.")
