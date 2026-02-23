
from fastapi import FastAPI
from app.routers import chat
from app.core.logging_config import setup_logging
from app.core.exception_handler import register_exception_handlers


setup_logging()

app = FastAPI(title="HuggingFace Chat API")

app.include_router(chat.router)

register_exception_handlers(app)
import uvicorn
if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)

