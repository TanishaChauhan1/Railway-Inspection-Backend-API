# Railway-Inspection-Backend-API


This is a backend system built using **FastAPI**, **SQLAlchemy**, and **PostgreSQL**. It handles form submissions for:

- **Bogie Checksheet**
- **Wheel Specifications**

Each form submission is stored in a PostgreSQL database using a structured JSON format where applicable.

---

## 📦 Tech Stack

- **FastAPI** – Web framework
- **PostgreSQL** – Relational database
- **SQLAlchemy** – ORM for DB models
- **Pydantic** – Schema validation
- **Uvicorn** – ASGI server

---

## 📁 Project Structure
app/
├── crud.py # DB interaction logic
├── database.py # Database engine/session setup
├── models.py # SQLAlchemy models
├── routes.py # FastAPI routes
├── schemas.py # Pydantic schemas
└── main.py # App entry point

## 🚀 Getting Started

### 1. Clone the repo

git clone <repo-url>
cd <project-folder>

### 2. Set up a virtual environment (optional but recommended)

python -m venv venv
source venv\Scripts\activate

### 3. Install dependencies

pip install -r requirements.txt

### 4. Set up PostgreSQL

Create a PostgreSQL database named (for example) inspection_db.

Update DATABASE_URL in database.py:
DATABASE_URL = "postgresql://<user>:<password>@localhost:5432/inspection_db"

### 5. Initialize database tables

Make sure the database is running, then run:
# Add this to a script or use the FastAPI startup
from app.database import Base, engine
Base.metadata.create_all(bind=engine)

Or manually invoke table creation inside main.py before running the server.

# 🛠 Endpoints
## 🚂 /forms/bogie-checksheet (POST)
Accepts Bogie Checksheet form data

Nested bogieDetails, bogieChecksheet, and bmbcChecksheet

### Sample Payload

{
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

## ⚙️ /forms/wheel-specifications (POST)
Accepts Wheel Specification data

fields is a nested object

### Sample Payload

{
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
  }
}

# ▶️ Running the Server

uvicorn app.main:app --reload

## App will be available at: http://localhost:8000

# 📓 Notes
Ensure the DB schema matches column names defined in models.py

If schema mismatch errors occur (e.g., formNumber vs form_number), drop and recreate the affected tables

Use tools like Postman or Swagger UI (/docs) to test endpoints
