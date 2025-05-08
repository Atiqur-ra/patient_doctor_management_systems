from sqlalchemy.orm import Session
from app.models.medicine import Medicine
from app.schemas.medicine import MedicineCreate

# Create a new medicine
def create_medicine(db: Session, medicine: MedicineCreate) -> Medicine:
    db_medicine = Medicine(**medicine.dict())
    db.add(db_medicine)
    db.commit()
    db.refresh(db_medicine)
    return db_medicine

# Get all medicines
def get_all_medicines(db: Session):
    return db.query(Medicine).all()

# Get a specific medicine by ID
def get_medicine_by_id(db: Session, medicine_id: int) -> Medicine:
    return db.query(Medicine).filter(Medicine.id == medicine_id).first()

# Update a medicine's details
def update_medicine(db: Session, medicine_id: int, medicine: MedicineCreate) -> Medicine:
    db_medicine = db.query(Medicine).filter(Medicine.id == medicine_id).first()
    if db_medicine:
        for key, value in medicine.dict().items():
            setattr(db_medicine, key, value)
        db.commit()
        db.refresh(db_medicine)
    return db_medicine

# Delete a medicine by ID
def delete_medicine(db: Session, medicine_id: int):
    db_medicine = db.query(Medicine).filter(Medicine.id == medicine_id).first()
    if db_medicine:
        db.delete(db_medicine)
        db.commit()
    return db_medicine

# Search for medicines by name
def search_medicines(db: Session, name: str):
    return db.query(Medicine).filter(Medicine.name.ilike(f"%{name}%")).all()


def add_medicine(db: Session, medicine: MedicineCreate):
    db_medicine = Medicine(
        name=medicine.name,
        description=medicine.description,
        price=medicine.price
    )
    db.add(db_medicine)
    db.commit()
    db.refresh(db_medicine)
    return db_medicine
