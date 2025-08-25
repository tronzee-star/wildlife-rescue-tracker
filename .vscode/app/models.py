from __future__ import annotations

from sqlalchemy import String, Integer, ForeignKey, Date
from sqlalchemy.orm import declarative_base, relationship, Mapped, mapped_column

Base = declarative_base()

class Species(Base):
    __tablename__ = "species"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    category: Mapped[str] = mapped_column(String, nullable=False)

    rescues: Mapped[list[Rescue]] = relationship(back_populates="species")
    populations: Mapped[list[Population]] = relationship(back_populates="species")

class Location(Base):
    __tablename__ = "locations"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    region: Mapped[str | None] = mapped_column(String, nullable=True)

    rescues: Mapped[list[Rescue]] = relationship(back_populates="location")
    populations: Mapped[list[Population]] = relationship(back_populates="location")
