from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.user import UserCreate
from app.crud.user import create_user
from app.database import get_db
router = APIRouter(prefix="/users", tags=["users"])

@router.post("/")
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db, user)
