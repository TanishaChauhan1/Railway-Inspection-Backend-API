# app/models.py

from sqlalchemy import Column, Integer, String, Float, JSON, Date
from app.database import Base

class BogieForm(Base):
    __tablename__ = "bogie_forms"

    id = Column(Integer, primary_key=True, index=True)
    formNumber = Column(String, unique=True, nullable=False)
    inspectionBy = Column(String, nullable=False)
    inspectionDate = Column(Date, nullable=False)
    bogieDetails = Column(JSON, nullable=False)
    bogieChecksheet = Column(JSON, nullable=False)
    bmbcChecksheet = Column(JSON, nullable=False)

class WheelSpecification(Base):
    __tablename__ = "wheel_specifications"

    id = Column(Integer, primary_key=True, index=True)
    formNumber = Column(String)
    submittedBy = Column(String)
    submittedDate = Column(Date)
    fields = Column(JSON)
    inspector = Column(String)
    location = Column(String)
    remarks = Column(String)
    status = Column(String)