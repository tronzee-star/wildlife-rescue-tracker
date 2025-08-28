from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

# -------- Location Model --------
class Location(Base):
    __tablename__ = "locations"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    region = Column(String, nullable=False)

    rescue_centers = relationship("RescueCenter", back_populates="location")

# -------- Rescue Center Model --------
class RescueCenter(Base):
    __tablename__ = "rescue_centers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    location_id = Column(Integer, ForeignKey("locations.id"))

    location = relationship("Location", back_populates="rescue_centers")
    animals = relationship("Animal", back_populates="rescue_center")

# -------- Animal Model --------
class Animal(Base):
    __tablename__ = "animals"

    id = Column(Integer, primary_key=True, index=True)
    species = Column(String, nullable=False)
    name = Column(String, nullable=False)
    rescue_center_id = Column(Integer, ForeignKey("rescue_centers.id"))

    rescue_center = relationship("RescueCenter", back_populates="animals")
