from fastapi import APIRouter
from app.schemas.request import GenerateRequest, GenerateResponse
from app.services.llm_service import LLMService

router = APIRouter()
llm_service = LLMService()

@router.post("/post-generate", response_model=GenerateResponse)
def generate_text(request: GenerateRequest):
    result = llm_service.generate(request.topic)
    return GenerateResponse(result=result)