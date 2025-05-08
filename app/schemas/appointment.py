from pydantic import BaseModel
from datetime import datetime

# ---------- Input schema (from client)
class AppointmentCreate(BaseModel):
    doctor_id: int
    patient_id: int
    appointment_time: datetime
    reason: str

# ---------- Output schema (to client)
class AppointmentOut(BaseModel):
    id: int
    doctor_id: int
    patient_id: int
    appointment_time: datetime
    reason: str
    status: str

    class Config:
        orm_mode = True  # Enable ORM-to-Pydantic conversion
