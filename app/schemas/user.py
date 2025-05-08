from pydantic import BaseModel, EmailStr
from enum import Enum

# Enum for user roles
class Role(str, Enum):
    admin = "admin"
    doctor = "doctor"
    patient = "patient"

# User registration model
class UserCreate(BaseModel):
    email: EmailStr
    password: str
    full_name: str
    role: Role

# Used for reading user info (response)
class UserOut(BaseModel):
    id: int
    email: EmailStr
    full_name: str
    role: Role

    class Config:
        orm_mode = True  # allows ORM-to-Pydantic conversion

# Internal use (e.g., for JWT)
class UserInDB(UserOut):
    hashed_password: str
