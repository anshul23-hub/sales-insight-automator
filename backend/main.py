from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
import pandas as pd
from ai_service import generate_summary
from email_service import send_email
from pydantic import EmailStr
import google.generativeai as genai
import os

genai.configure(api_key="AIzaSyDH9o2hVQ7TKksNQI2zBSR5ABNrX66YJrM")
app = FastAPI(title="Sales Insight Automator")

@app.get("/")
def root():
    return {"message": "Sales Insight Automator API Running"}

@app.post("/upload")
async def upload_file(file: UploadFile = File(...), email: EmailStr = Form(...)):

    if not file.filename.endswith(".csv"):
        raise HTTPException(status_code=400, detail="Only CSV files allowed")

    try:

        df = pd.read_csv(file.file)

        summary = generate_summary(df)

        send_email(email, summary)

        return {
            "status": "success",
            "summary": summary
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))