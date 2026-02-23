from fastapi import APIRouter
from app.schemas.chat_schema import ChatRequest, ChatResponse
from app.services.chat_service import ChatService

router = APIRouter()
chat_service = ChatService()

@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    response = chat_service.ask(request.message)
    return ChatResponse(response=response)

@router.post("/textclassifier", response_model=ChatResponse)
def chat(request: ChatRequest):
    response = chat_service.textclassifier(request.message)
    return ChatResponse(response=response)