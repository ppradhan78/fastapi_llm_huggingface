import json

from app.utility.hf_client import get_hf_client
from app.core.config import settings
import logging

logger = logging.getLogger(__name__)
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

    def textclassifier(self, message: str) -> str:
        logger.info("message"+message)
        logger.info("model" + settings.model_name_textclassifier)
        try:
            completion = self.client.text_classification(
            message,
            model=settings.model_name_textclassifier
            )
            logger.info("completion" + json.dumps(completion, indent=2))
            max_item = max(completion, key=lambda x: x["score"])
            logger.info("max_item" + json.dumps(max_item, indent=2))
            return json.dumps(max_item, indent=2)
        except Exception as e:
            logger.error("Error while generating response"+e, exc_info=True)
        raise