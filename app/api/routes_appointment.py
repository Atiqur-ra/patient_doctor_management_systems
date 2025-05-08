from fastapi import APIRouter
from app.schemas.appointment import AppointmentCreate
from app.crud.appointment import book_appointment

router = APIRouter(prefix="/appointments", tags=["appointments"])

@router.post("/")
def create_appointment(data: AppointmentCreate):
    return book_appointment(data)
