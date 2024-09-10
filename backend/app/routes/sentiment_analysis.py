from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.models.llm_models import get_sentiment_analysis_model

router = APIRouter()

class SentimentAnalysisRequest(BaseModel):
    input: str
    model: str

class SentimentAnalysisResponse(BaseModel):
    sentiment: str
    score: float

@router.post("/analyze-sentiment", response_model=SentimentAnalysisResponse)
async def analyze_sentiment(request: SentimentAnalysisRequest):
    try:
        model = get_sentiment_analysis_model(request.model)
        result = model.analyze(request.input)
        return SentimentAnalysisResponse(**result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))