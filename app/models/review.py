from sqlalchemy import Column, Integer, ForeignKey, String, Float
from app.database import Base

class Review(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True)
    doctor_id = Column(Integer, ForeignKey("users.id"))
    patient_id = Column(Integer, ForeignKey("users.id"))
    rating = Column(Float)
    comment = Column(String)