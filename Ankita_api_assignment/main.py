# main.py
from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from typing import Optional, List, Dict
from datetime import date
from sqlalchemy.orm import Session
from database import SessionLocal, engine, Base
import models

Base.metadata.create_all(bind=engine)

app = FastAPI()

# CORS (optional, for local frontend testing)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ------------------ Pydantic Schemas ------------------
class WheelFields(BaseModel):
    treadDiameterNew: str
    lastShopIssueSize: str
    condemningDia: str
    wheelGauge: str
    variationSameAxle: str
    variationSameBogie: str
    variationSameCoach: str
    wheelProfile: str
    intermediateWWP: str
    bearingSeatDiameter: str
    rollerBearingOuterDia: str
    rollerBearingBoreDia: str
    rollerBearingWidth: str
    axleBoxHousingBoreDia: str
    wheelDiscWidth: str

class WheelSpecCreate(BaseModel):
    formNumber: str
    submittedBy: str
    submittedDate: date
    fields: WheelFields

class BogieDetails(BaseModel):
    bogieNo: str
    makerYearBuilt: str
    incomingDivAndDate: str
    deficitComponents: str
    dateOfIOH: str

class BogieChecksheet(BaseModel):
    bogieFrameCondition: str
    bolster: str
    bolsterSuspensionBracket: str
    lowerSpringSeat: str
    axleGuide: str

class BMBCChecksheet(BaseModel):
    cylinderBody: str
    pistonTrunnion: str
    adjustingTube: str
    plungerSpring: str

class BogieFormCreate(BaseModel):
    formNumber: str
    inspectionBy: str
    inspectionDate: date
    bogieDetails: BogieDetails
    bogieChecksheet: BogieChecksheet
    bmbcChecksheet: BMBCChecksheet

# ------------------ API Routes ------------------
@app.post("/api/forms/wheel-specifications")
def submit_wheel_spec(form: WheelSpecCreate, db: Session = Depends(get_db)):
    db_form = models.WheelSpecification(**form.dict(), status="Saved")
    db.add(db_form)
    db.commit()
    return {
        "success": True,
        "message": "Wheel specification submitted successfully.",
        "data": {
            "formNumber": form.formNumber,
            "submittedBy": form.submittedBy,
            "submittedDate": str(form.submittedDate),
            "status": "Saved"
        }
    }

@app.get("/api/forms/wheel-specifications")
def get_wheel_specs(formNumber: Optional[str] = None, submittedBy: Optional[str] = None, submittedDate: Optional[date] = None, db: Session = Depends(get_db)):
    query = db.query(models.WheelSpecification)
    if formNumber:
        query = query.filter(models.WheelSpecification.formNumber == formNumber)
    if submittedBy:
        query = query.filter(models.WheelSpecification.submittedBy == submittedBy)
    if submittedDate:
        query = query.filter(models.WheelSpecification.submittedDate == submittedDate)
    results = query.all()
    return {
        "success": True,
        "message": "Filtered wheel specification forms fetched successfully.",
        "data": [
            {
                "formNumber": r.formNumber,
                "submittedBy": r.submittedBy,
                "submittedDate": str(r.submittedDate),
                "fields": r.fields
            } for r in results
        ]
    }

@app.post("/api/forms/bogie-checksheet")
def submit_bogie_form(form: BogieFormCreate, db: Session = Depends(get_db)):
    db_form = models.BogieChecksheetModel(**form.dict(), status="Saved")
    db.add(db_form)
    db.commit()
    return {
        "success": True,
        "message": "Bogie checksheet submitted successfully.",
        "data": {
            "formNumber": form.formNumber,
            "inspectionBy": form.inspectionBy,
            "inspectionDate": str(form.inspectionDate),
            "status": "Saved"
        }
    }
