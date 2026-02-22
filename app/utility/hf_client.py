from huggingface_hub import InferenceClient
from app.core.config import settings

def get_hf_client():
    return InferenceClient(api_key=settings.hf_token)