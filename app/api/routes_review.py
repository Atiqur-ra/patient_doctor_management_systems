from fastapi import APIRouter
from app.schemas.review import ReviewCreate
from app.crud.review import add_review

router = APIRouter(prefix="/reviews", tags=["reviews"])

@router.post("/")
def create_review(data: ReviewCreate):
    return add_review(data)
