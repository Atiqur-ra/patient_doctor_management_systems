from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

# Input schema for creating a review
class ReviewCreate(BaseModel):
    doctor_id: int
    rating: int = Field(..., ge=1, le=5, description="Rating must be between 1 and 5")
    comment: Optional[str] = None

# Output schema for a single review
class ReviewOut(BaseModel):
    id: int
    patient_id: int
    doctor_id: int
    rating: int
    comment: Optional[str]
    created_at: datetime

    class Config:
        orm_mode = True
