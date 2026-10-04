from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from database import check_number, report_number

app = FastAPI(title="Phone Recycle Detector API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class PhoneRequest(BaseModel):
    phone: str

class ReportRequest(BaseModel):
    phone: str
    issue: str

@app.get("/")
def home():
    return {"message": "Phone Recycle Detector API is running"}

@app.post("/check")
def check(req: PhoneRequest):
    return check_number(req.phone)

@app.post("/report")
def report(req: ReportRequest):
    return report_number(req.phone, req.issue)

# Run: uvicorn main:app --reload --port 8000