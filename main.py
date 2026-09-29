import os
import sys
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional

# Ensure backend directory is in python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from database import init_db, save_history, get_history
from waste_logic import analyze_waste_input

app = FastAPI(
    title="Smart Waste Management Assistant API",
    description="Backend API for waste identification, environmental impact analysis, and disposal guidance.",
    version="1.0.0"
)

# Allow Cross-Origin Resource Sharing
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
def startup_event():
    """Initialize database on application startup."""
    init_db()


class WasteAnalyzeRequest(BaseModel):
    waste_type: Optional[str] = None
    waste_item: Optional[str] = None


@app.get("/api/health")
def health():
    """Health check endpoint."""
    return {"status": "running"}


@app.post("/api/analyze")
def analyze(payload: WasteAnalyzeRequest):
    """
    Analyzes waste item input, returns category & disposal instructions,
    and stores record in SQLite history.
    """
    input_text = payload.waste_type or payload.waste_item or ""
    if not input_text or not input_text.strip():
        raise HTTPException(
            status_code=400,
            detail="Unable to identify the waste type. Please provide more details or select a common waste type."
        )

    result = analyze_waste_input(input_text.strip())

    # Save to SQLite database
    try:
        save_history(
            waste_item=input_text.strip(),
            category=result.get("waste_category", "Unclassified"),
            disposal_method=result.get("disposal_method", "N/A")
        )
    except Exception as e:
        print(f"[Warning] DB save error: {e}")

    return result


@app.get("/api/history")
def history():
    """Returns stored waste analysis records."""
    return get_history()
