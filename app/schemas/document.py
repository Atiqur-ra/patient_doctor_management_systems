from pydantic import BaseModel
from datetime import datetime

class DocumentCreate(BaseModel):
    file_path: str
    file_type: str
    owner_id: int

class DocumentOut(BaseModel):
    id: int
    file_path: str
    file_type: str
    uploaded_at: datetime
    owner_id: int

    class Config:
        orm_mode = True
