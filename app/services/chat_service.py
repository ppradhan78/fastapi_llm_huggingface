from app.utility.hf_client import get_hf_client
from app.core.config import settings

class ChatService:

    def __init__(self):
        self.client = get_hf_client()

    def ask(self, message: str) -> str:
        completion = self.client.chat.completions.create(
            model=settings.model_name,
            messages=[{"role": "user", "content": message}],
            max_tokens=settings.max_tokens,
        )

        return completion.choices[0].message.content