from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List
import json
from pathlib import Path

router = APIRouter()

class FeedbackItem(BaseModel):
    modelType: str
    modelName: str
    rating: int
    comment: str

# JSON file used instead of actual DB (in Prod implement connect and using an actual DB)
FEEDBACK_FILE = Path("feedback.json")

def load_feedback():
    if FEEDBACK_FILE.exists():
        with open(FEEDBACK_FILE, "r") as f:
            return json.load(f)
    return []

def save_feedback(feedback):
    with open(FEEDBACK_FILE, "w") as f:
        json.dump(feedback, f)

@router.post("/submit-feedback")
async def submit_feedback(feedback: FeedbackItem):
    try:
        all_feedback = load_feedback()
        all_feedback.append(feedback.dict())
        save_feedback(all_feedback)
        return {"message": "Feedback submitted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/get-feedback", response_model=List[FeedbackItem])
async def get_feedback():
    try:
        return load_feedback()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))