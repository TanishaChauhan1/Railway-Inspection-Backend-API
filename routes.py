# app/routes.py

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app import schemas, crud
from fastapi import HTTPException

router = APIRouter()

# --- Bogie Checksheet ---

@router.post("/forms/bogie-checksheet", response_model=schemas.BogieFormSchema)
def submit_bogie_form(data: schemas.BogieFormSchema, db: Session = Depends(get_db)):
    try:
        return crud.create_bogie_form(db, data)
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))

# --- Wheel Specifications ---
@router.post("/forms/wheel-specifications", response_model=schemas.WheelSpecBase)
def submit_wheel_spec(data: schemas.WheelSpecBase, db: Session = Depends(get_db)):
    try:
        return crud.create_wheel_spec(db, data)
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))

