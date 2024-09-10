from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List
from app.models.llm_models import get_ner_model

router = APIRouter()

class NERRequest(BaseModel):
    input: str
    model: str

class Entity(BaseModel):
    entity: str
    start: int
    end: int
    label: str

class NERResponse(BaseModel):
    entities: List[Entity]

@router.post("/perform-ner", response_model=NERResponse)
async def perform_ner(request: NERRequest):
    try:
        model = get_ner_model(request.model)
        entities = model.extract_entities(request.input)
        return NERResponse(entities=[Entity(**entity) for entity in entities])
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))