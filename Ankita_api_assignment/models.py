# models.py
from sqlalchemy import Column, Integer, String, Date, JSON
from database import Base

class WheelSpecification(Base):
    __tablename__ = "wheel_specifications"
    id = Column(Integer, primary_key=True, index=True)
    formNumber = Column(String, unique=True, index=True)
    submittedBy = Column(String)
    submittedDate = Column(Date)
    fields = Column(JSON)
    status = Column(String)

class BogieChecksheetModel(Base):
    __tablename__ = "bogie_checksheet"
    id = Column(Integer, primary_key=True, index=True)
    formNumber = Column(String, unique=True, index=True)
    inspectionBy = Column(String)
    inspectionDate = Column(Date)
    bogieDetails = Column(JSON)
    bogieChecksheet = Column(JSON)
    bmbcChecksheet = Column(JSON)
    status = Column(String)
