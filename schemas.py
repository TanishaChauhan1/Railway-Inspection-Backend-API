# app/schemas.py

from datetime import date
from typing import Optional
from pydantic import BaseModel, Field


# --- Nested Models for Bogie Form ---
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

class BogieFormSchema(BaseModel):
    formNumber: str
    inspectionBy: str
    inspectionDate: date
    bogieDetails: BogieDetails
    bogieChecksheet: BogieChecksheet
    bmbcChecksheet: BMBCChecksheet

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "formNumber": "BOGIE-2025-001",
                "inspectionBy": "user_id_456",
                "inspectionDate": "2025-07-03",
                "bogieDetails": {
                    "bogieNo": "BG1234",
                    "makerYearBuilt": "RDSO/2018",
                    "incomingDivAndDate": "NR / 2025-06-25",
                    "deficitComponents": "None",
                    "dateOfIOH": "2025-07-01"
                },
                "bogieChecksheet": {
                    "bogieFrameCondition": "Good",
                    "bolster": "Good",
                    "bolsterSuspensionBracket": "Cracked",
                    "lowerSpringSeat": "Good",
                    "axleGuide": "Worn"
                },
                "bmbcChecksheet": {
                    "cylinderBody": "WORN OUT",
                    "pistonTrunnion": "GOOD",
                    "adjustingTube": "DAMAGED",
                    "plungerSpring": "GOOD"
                }
            }
        }

# --- Wheel Specifications ---

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

class WheelSpecBase(BaseModel):
    formNumber: str
    submittedBy: str
    submittedDate: date
    fields: WheelFields
    inspector: Optional[str] = None
    location: Optional[str] = None
    remarks: Optional[str] = None
    status: Optional[str] = None

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "formNumber": "WHEEL-2025-001",
                "submittedBy": "user_id_123",
                "submittedDate": "2025-07-03",
                "fields": {
                    "treadDiameterNew": "915 (900-1000)",
                    "lastShopIssueSize": "837 (800-900)",
                    "condemningDia": "825 (800-900)",
                    "wheelGauge": "1600 (+2,-1)",
                    "variationSameAxle": "0.5",
                    "variationSameBogie": "5",
                    "variationSameCoach": "13",
                    "wheelProfile": "29.4 Flange Thickness",
                    "intermediateWWP": "20 TO 28",
                    "bearingSeatDiameter": "130.043 TO 130.068",
                    "rollerBearingOuterDia": "280 (+0.0/-0.035)",
                    "rollerBearingBoreDia": "130 (+0.0/-0.025)",
                    "rollerBearingWidth": "93 (+0/-0.250)",
                    "axleBoxHousingBoreDia": "280 (+0.030/+0.052)",
                    "wheelDiscWidth": "127 (+4/-0)"
                },
                "inspector": None,
                "location": None,
                "remarks": None,
                "status": None
            }
        }
