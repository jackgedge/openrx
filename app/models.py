from typing import List
from datetime import datetime
from sqlalchemy import ForeignKey, String, Date, DateTime
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from flask_login import UserMixin

# Declare base for metadata
class Base(DeclarativeBase):
    pass

# Create user_account table
class User(UserMixin, Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True)
    last_name: Mapped[str] = mapped_column(String(30))
    first_name: Mapped[str] = mapped_column(String(30))
    username: Mapped[str] = mapped_column(String(30), unique=True, nullable=False)
    password_hash: Mapped[str] 
    addresses: Mapped[List["Address"]] = relationship(
        back_populates="user", cascade="all, delete-orphan"
    )
    def __repr__(self) -> str:
        return f"User(id={self.id!r}, username={self.username!r}, first_name={self.first_name!r}, last_name={self.last_name!r})"

# Create address table
class Address(Base):
    __tablename__ = "address"
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str]
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    user: Mapped["User"] = relationship(back_populates="addresses")
    def __repr__(self) -> str:
        return f"Address(id={self.id!r}, email={self.email!r})"

# Create patient table
class Patient(Base):
    __tablename__ = "patient"
    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(String(30))
    last_name: Mapped[str] = mapped_column(String(30))
    dob: Mapped[Date] = mapped_column(Date)

    encounters = relationship("Encounter", back_populates="patient")

class Encounter(Base):
    __tablename__ = "encounter"
    id: Mapped[int] = mapped_column(primary_key=True)
    patient_id: Mapped[int] = mapped_column(ForeignKey("patient.id"))
    pc: Mapped[str]
    hpc: Mapped[str]
    exam: Mapped[str]
    hr: Mapped[int]
    sbp: Mapped[int]
    dbp: Mapped[int]
    rr: Mapped[int]
    temp: Mapped[float]
    cbg: Mapped[float]
    gcs_e: Mapped[int]
    gcs_v: Mapped[int]
    gcs_m: Mapped[int]
    diagnosis_1: Mapped[str]
    icd_11_1: Mapped[str]
    tx: Mapped[str]
    outcome: Mapped[str]
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    patient = relationship("Patient", back_populates="encounters")

    def __repr__(self) -> str:
        return f"Encounter(id={self.id!r}, patient_id={self.patient_id!r}, outcome={self.outcome!r})"

class Note(Base):
    __tablename__ = "note"
    id: Mapped[int] = mapped_column(primary_key=True)
    patient_id: Mapped[int] = mapped_column(ForeignKey("patient.id"))
    note: Mapped[str]
    author_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"Note(id={self.id!r}, patient_id={self.patient_id!r}, note={self.note!r}, author_id={self.author_id!r}, created_at={self.created_at!r})"

def create_tables(engine):
    Base.metadata.create_all(engine) 