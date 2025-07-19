Backend API was tested independently via Postman.
🚆 Wheel & Bogie Inspection API (FastAPI + PostgreSQL)
This FastAPI project provides API endpoints to submit and retrieve wheel specifications and bogie inspection forms. It uses SQLAlchemy for ORM and stores complex form data as JSON in a PostgreSQL database.

✅ Technologies Used
FastAPI – for creating high-performance REST APIs

Pydantic – for data validation

SQLAlchemy – ORM for interacting with PostgreSQL

PostgreSQL – backend database

Uvicorn – ASGI server for running FastAPI

dotenv – to load environment variables

CORS Middleware – for frontend/backend integration

Postman – for API testing

🚀 Project Setup Steps

1.Clone the repository:

git clone https://github.com/ankitashelke007/Ankita_api_assignment.git

cd Ankita_api_assignment

2.Create and activate a virtual environment:

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3.Install dependencies:

pip install fastapi uvicorn python-dotenv sqlalchemy psycopg2 pydantic

4.Configure your .env file:
Create a .env file in the project root with the following:

DATABASE_URL=postgresql://postgres:Ankita%4045@localhost:5432/demo

5.Run the application:

uvicorn main:app --reload

6.Test the APIs:
Open your browser or Postman and use:

http://127.0.0.1:8000/docs
to explore Swagger UI.

📄 API Endpoints
1. Submit Wheel Specification Form
Endpoint: POST /api/forms/wheel-specifications

Request Body:
{
  "formNumber": "BCF005",
  "submittedBy": "Ankita",
  "submittedDate": "2025-07-18",
  "fields": {
    "treadDiameterNew": "960mm",
    "lastShopIssueSize": "950mm",
    "condemningDia": "850mm",
    "wheelGauge": "1676mm",
    "variationSameAxle": "2mm",
    "variationSameBogie": "3mm",
    "variationSameCoach": "5mm",
    "wheelProfile": "OK",
    "intermediateWWP": "920mm",
    "bearingSeatDiameter": "100mm",
    "rollerBearingOuterDia": "120mm",
    "rollerBearingBoreDia": "90mm",
    "rollerBearingWidth": "30mm",
    "axleBoxHousingBoreDia": "110mm",
    "wheelDiscWidth": "125mm"
  }
}
Response: Confirmation message with status Saved.

2. Get Wheel Specification Forms (with filters)
Endpoint: GET /api/forms/wheel-specifications

Query Params (optional): formNumber, submittedBy, submittedDate

Example:

/api/forms/wheel-specifications?formNumber=BCF002
Response: List of matching forms with wheel fields.

3. Submit Bogie Checksheet Form
Endpoint: POST /api/forms/bogie-checksheet

Request Body:
{
  "formNumber": "BG101",
  "inspectionBy": "InspectorA",
  "inspectionDate": "2025-07-18",
  "bogieDetails": {
    "bogieNo": "B123",
    "makerYearBuilt": "ICF 2010",
    "incomingDivAndDate": "WR 2025-07-10",
    "deficitComponents": "None",
    "dateOfIOH": "2025-07-15"
  },
  "bogieChecksheet": {
    "bogieFrameCondition": "OK",
    "bolster": "Good",
    "bolsterSuspensionBracket": "OK",
    "lowerSpringSeat": "OK",
    "axleGuide": "OK"
  },
  "bmbcChecksheet": {
    "cylinderBody": "Good",
    "pistonTrunnion": "OK",
    "adjustingTube": "OK",
    "plungerSpring": "OK"
  }
}
Response: Confirmation message with status Saved.

🔍 Assumptions & Notes

The project assumes a local PostgreSQL instance running with database demo.

The fields and other complex form data are stored as JSON for flexibility.

Each form has a unique formNumber (validated via DB unique index).

No user authentication is implemented (can be added as future enhancement).

API responses are standardized with success, message, and data.

🧪 Testing
You can use the included Postman collection named KPA_form data to:

1.Test GET and POST for Wheel Specification
2.Test POST for Bogie Checksheet

📂 Folder Structure 
.
├── main.py
├── models.py
├── database.py
├── .env
├── requirements.txt
├── README.md
└── postman_collection.json (optional)
⚠️ Due to plartform limitations or environment constraints, the provided Flutter frontend (https://github.com/s2pl/KPA-ERP-FE/) was not run or integrated with the backend.

However, the implemented APIs strictly follow the structure and data format specified in the SwaggerHub documentation and Postman collection. All endpoints have been thoroughly tested using Postman, and the responses are aligned with the expected frontend usage.

The backend is fully ready to integrate with the frontend without requiring any changes.

