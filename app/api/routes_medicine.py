from fastapi import APIRouter
from app.schemas.medicine import MedicineCreate
from app.crud.medicine import add_medicine

router = APIRouter(prefix="/medicines", tags=["medicines"])

@router.post("/")
def create_medicine(data: MedicineCreate):
    return add_medicine(data)
