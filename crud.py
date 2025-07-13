# app/crud.py

from sqlalchemy.orm import Session
from app import models, schemas

# --- Bogie Checksheet ---

def create_bogie_form(db: Session, form: schemas.BogieFormSchema):
    db_form = models.BogieForm(
        formNumber=form.formNumber,
        inspectionBy=form.inspectionBy,
        inspectionDate=form.inspectionDate,
        bogieDetails=form.bogieDetails.dict(),
        bogieChecksheet=form.bogieChecksheet.dict(),
        bmbcChecksheet=form.bmbcChecksheet.dict()
    )
    db.add(db_form)
    db.commit()
    db.refresh(db_form)
    return db_form

# --- Wheel Specifications ---
def create_wheel_spec(db: Session, form_data: schemas.WheelSpecBase):
    new_entry = models.WheelSpecification(
        formNumber=form_data.formNumber,
        submittedBy=form_data.submittedBy,
        submittedDate=form_data.submittedDate,
        fields=form_data.fields.dict(),
        inspector=form_data.inspector,
        location=form_data.location,
        remarks=form_data.remarks,
        status=form_data.status
    )
    db.add(new_entry)
    db.commit()
    db.refresh(new_entry)
    return new_entry