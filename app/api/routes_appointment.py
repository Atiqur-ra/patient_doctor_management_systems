from fastapi import APIRouter, Depends, HTTPException, status
from app.schemas.appointment import AppointmentCreate
from app.crud.appointment import book_appointment
from app.services.auth import get_current_user
from app.models.user import User
from app.crud.appointment import get_doctor_availability

router = APIRouter(prefix="/appointments", tags=["appointments"])

@router.post("/")
def create_appointment(data: AppointmentCreate, current_user: User = Depends(get_current_user)):
    # Check if current user is a patient before booking an appointment
    if current_user.role != 'patient':
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Only patients can book appointments.")
    return book_appointment(data, current_user)

@router.get("/doctor/{doctor_id}/availability")
def get_availability(doctor_id: int, current_user: User = Depends(get_current_user)):
    if current_user.role != "patient":
        raise HTTPException(status_code=403, detail="Only patients can check doctor availability.")
    
    db = SessionLocal()
    available_dates = get_doctor_availability(db, doctor_id)
    
    if not available_dates:
        raise HTTPException(status_code=404, detail="No availability found for this doctor.")
    
    return {"available_dates": [availability.available_date for availability in available_dates]}
