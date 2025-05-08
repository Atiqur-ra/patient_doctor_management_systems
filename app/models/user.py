from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from enum import Enum as PyEnum
from app.database import Base
from app.models.appointment import Appointment
from app.models.document import Document
from sqlalchemy import DateTime

# Enum for User roles
class Role(PyEnum):
    admin = "admin"
    doctor = "doctor"
    patient = "patient"

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    full_name = Column(String, nullable=False)
    role = Column(String, nullable=False)  # 'patient' or 'doctor'
    is_active = Column(Integer, default=1)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    # Relationships
    # Specify foreign keys to avoid ambiguity in appointments relationship
    appointments_as_patient = relationship(
    "Appointment",
    back_populates="patient",
    foreign_keys=[Appointment.patient_id]
)

    appointments_as_doctor = relationship(
        "Appointment",
        back_populates="doctor",
        foreign_keys=[Appointment.doctor_id]
    )
    
    documents = relationship("Document", back_populates="owner")
