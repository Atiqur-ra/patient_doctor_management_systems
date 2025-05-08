from sqlalchemy.orm import Session
from datetime import datetime
from app.models.appointment import Appointment
from app.schemas.appointment import AppointmentCreate

# Create a new appointment
def book_appointment(db: Session, appointment: AppointmentCreate) -> Appointment:
    db_appointment = Appointment(
        doctor_id=appointment.doctor_id,
        patient_id=appointment.patient_id,
        appointment_time=appointment.appointment_time,
        reason=appointment.reason,
        status="booked"
    )
    db.add(db_appointment)
    db.commit()
    db.refresh(db_appointment)
    return db_appointment

# Get all appointments for a patient
def get_patient_appointments(db: Session, patient_id: int):
    return db.query(Appointment).filter(Appointment.patient_id == patient_id).all()

# Get all appointments for a doctor
def get_doctor_appointments(db: Session, doctor_id: int):
    return db.query(Appointment).filter(Appointment.doctor_id == doctor_id).all()

# Get future appointments
def get_future_appointments(db: Session, user_id: int, role: str):
    now = datetime.utcnow()
    if role == "doctor":
        return db.query(Appointment).filter(Appointment.doctor_id == user_id, Appointment.appointment_time > now).all()
    else:
        return db.query(Appointment).filter(Appointment.patient_id == user_id, Appointment.appointment_time > now).all()

# Get past appointments
def get_past_appointments(db: Session, user_id: int, role: str):
    now = datetime.utcnow()
    if role == "doctor":
        return db.query(Appointment).filter(Appointment.doctor_id == user_id, Appointment.appointment_time <= now).all()
    else:
        return db.query(Appointment).filter(Appointment.patient_id == user_id, Appointment.appointment_time <= now).all()
