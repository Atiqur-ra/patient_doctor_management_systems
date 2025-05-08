from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app import crud
from app.schemas import review as review_schema
from app.dependencies import get_db, get_current_active_patient
from app.models.user import User

router = APIRouter(prefix="/reviews", tags=["Reviews"])

# Create a new review
@router.post("/", response_model=review_schema.ReviewOut)
def create_review(
    review: review_schema.ReviewCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_patient)  # Only patients allowed
):
    return crud.review.create_review(db, review=review, patient_id=current_user.id)

# Get all reviews for a specific doctor
@router.get("/doctor/{doctor_id}", response_model=List[review_schema.ReviewOut])
def get_reviews_for_doctor(
    doctor_id: int,
    db: Session = Depends(get_db)
):
    return crud.review.get_reviews_for_doctor(db, doctor_id)

# Get all reviews written by the logged-in patient
@router.get("/my", response_model=List[review_schema.ReviewOut])
def get_my_reviews(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_patient)
):
    return crud.review.get_reviews_by_patient(db, current_user.id)

# Get a single review by ID
@router.get("/{review_id}", response_model=review_schema.ReviewOut)
def get_review_by_id(review_id: int, db: Session = Depends(get_db)):
    review = crud.review.get_review_by_id(db, review_id)
    if not review:
        raise HTTPException(status_code=404, detail="Review not found")
    return review
