from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.models.llm_models import get_text_generation_model

router = APIRouter()

class TextGenerationRequest(BaseModel):
    input: str
    model: str

class TextGenerationResponse(BaseModel):
    generated_text: str

@router.post("/generate-text", response_model=TextGenerationResponse)
async def generate_text(request: TextGenerationRequest):
    try:
        model = get_text_generation_model(request.model)
        generated_text = model.generate(request.input)
        return TextGenerationResponse(generated_text=generated_text)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))