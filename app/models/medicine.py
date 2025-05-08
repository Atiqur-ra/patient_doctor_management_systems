from sqlalchemy import Column, Integer, String, Float, Date
from app.database import Base

class Medicine(Base):
    __tablename__ = "medicines"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    stock = Column(Integer)
    expiry_date = Column(Date)
    price = Column(Float)