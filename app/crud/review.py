from sqlalchemy.orm import Session
from app.models.review import Review
from app.schemas.review import ReviewCreate
from typing import List

# Create a new review
def create_review(db: Session, review: ReviewCreate, patient_id: int) -> Review:
    db_review = Review(
        patient_id=patient_id,
        doctor_id=review.doctor_id,
        rating=review.rating,
        comment=review.comment
    )
    db.add(db_review)
    db.commit()
    db.refresh(db_review)
    return db_review

# Get all reviews for a specific doctor
def get_reviews_for_doctor(db: Session, doctor_id: int) -> List[Review]:
    return db.query(Review).filter(Review.doctor_id == doctor_id).all()

# Get all reviews written by a specific patient
def get_reviews_by_patient(db: Session, patient_id: int) -> List[Review]:
    return db.query(Review).filter(Review.patient_id == patient_id).all()

# Get a single review by its ID
def get_review_by_id(db: Session, review_id: int) -> Review:
    return db.query(Review).filter(Review.id == review_id).first()

from sqlalchemy.orm import Session
from app.models.review import Review
from app.schemas.review import ReviewCreate

def add_review(db: Session, review: ReviewCreate, patient_id: int):
    db_review = Review(
        rating=review.rating,
        comment=review.comment,
        doctor_id=review.doctor_id,
        patient_id=patient_id
    )
    db.add(db_review)
    db.commit()
    db.refresh(db_review)
    return db_review

