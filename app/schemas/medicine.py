from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional

# Medicine creation schema (input)
class MedicineCreate(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    quantity_in_stock: int

# Medicine output schema (response to client)
class MedicineOut(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    price: float
    quantity_in_stock: int
    created_at: datetime

    class Config:
        orm_mode = True  # Enable ORM-to-Pydantic conversion

# Medicine list schema for querying (e.g., for search)
class MedicineList(BaseModel):
    medicines: List[MedicineOut]
