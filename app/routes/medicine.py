from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.crud import medicine as crud_medicine
from app.schemas.medicine import MedicineCreate, MedicineOut

router = APIRouter(prefix="/medicines", tags=["Medicines"])

# Route to create a new medicine
@router.post("/", response_model=MedicineOut)
def create_medicine(medicine: MedicineCreate, db: Session = Depends(get_db)):
    return crud_medicine.create_medicine(db, medicine)

# Route to get all medicines
@router.get("/", response_model=list[MedicineOut])
def get_medicines(db: Session = Depends(get_db)):
    return crud_medicine.get_all_medicines(db)

# Route to get a specific medicine by ID
@router.get("/{medicine_id}", response_model=MedicineOut)
def get_medicine(medicine_id: int, db: Session = Depends(get_db)):
    medicine = crud_medicine.get_medicine_by_id(db, medicine_id)
    if medicine is None:
        raise HTTPException(status_code=404, detail="Medicine not found")
    return medicine

# Route to update medicine details
@router.put("/{medicine_id}", response_model=MedicineOut)
def update_medicine(medicine_id: int, medicine: MedicineCreate, db: Session = Depends(get_db)):
    updated_medicine = crud_medicine.update_medicine(db, medicine_id, medicine)
    if updated_medicine is None:
        raise HTTPException(status_code=404, detail="Medicine not found")
    return updated_medicine

# Route to delete a medicine
@router.delete("/{medicine_id}", response_model=MedicineOut)
def delete_medicine(medicine_id: int, db: Session = Depends(get_db)):
    deleted_medicine = crud_medicine.delete_medicine(db, medicine_id)
    if deleted_medicine is None:
        raise HTTPException(status_code=404, detail="Medicine not found")
    return deleted_medicine

# Route to search medicines by name
@router.get("/search", response_model=list[MedicineOut])
def search_medicines(name: str, db: Session = Depends(get_db)):
    return crud_medicine.search_medicines(db, name)
