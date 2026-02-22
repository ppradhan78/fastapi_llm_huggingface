# import os
# from dotenv import load_dotenv
# from huggingface_hub import InferenceClient
#
# load_dotenv()  # This loads .env file
# client = InferenceClient(
#     api_key=os.getenv("HF_TOKEN")
# )
# completion = client.chat.completions.create(
#     model="Nanbeige/Nanbeige4.1-3B",
#     messages=[
#         {"role": "user", "content": "What is the capital of India?"}
#     ]
# )
# print(completion.choices[0].message)
#
# if __name__ == "__main__":
#       query = "What is the capital of India?"
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

