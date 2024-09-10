from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Dict
import random  # For demo purposes; replace with actual data if used in production

router = APIRouter()

class ModelPerformance(BaseModel):
    modelName: str
    avgAccuracy: float
    avgLatency: float
    userRating: float

class PerformanceData(BaseModel):
    textGeneration: List[ModelPerformance]
    sentimentAnalysis: List[ModelPerformance]
    namedEntityRecognition: List[ModelPerformance]

@router.get("/performance-data", response_model=PerformanceData)
async def get_performance_data():
    try:
        # Dummy data used. In prod this data would be fetched from DB
        def generate_random_performance(models):
            return [
                ModelPerformance(
                    modelName=model,
                    avgAccuracy=random.uniform(0.7, 0.99),
                    avgLatency=random.uniform(50, 500),
                    userRating=random.uniform(3.0, 5.0)
                ) for model in models
            ]

        return PerformanceData(
            textGeneration=generate_random_performance(['gpt2', 'bert', 't5']),
            sentimentAnalysis=generate_random_performance(['bert', 'roberta', 'distilbert']),
            namedEntityRecognition=generate_random_performance(['spacy', 'flair', 'stanford'])
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))