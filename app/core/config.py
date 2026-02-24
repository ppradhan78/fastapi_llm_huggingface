import os
import tomli
import logging
from pathlib import Path
from dotenv import load_dotenv

logger = logging.getLogger(__name__)

BASE_DIR = Path(__file__).resolve().parent.parent.parent
CONFIG_PATH = BASE_DIR / "config.toml"

load_dotenv()


class Settings:
    def __init__(self):
        logger.info("Loading application configuration...")

        try:
            if not CONFIG_PATH.exists():
                raise FileNotFoundError(f"Config file not found: {CONFIG_PATH}")

            with open(CONFIG_PATH, "rb") as f:
                config = tomli.load(f)

            self.model_name = config["model"]["name"]
            self.model_name_textclassifier=config["model"]["textclassifier"]
            self.model_name_summarization=config["model"]["summarization"]
            self.max_tokens = config["model"]["max_tokens"]
            self.hf_token = os.getenv("HF_TOKEN")

            if not self.hf_token:
                raise ValueError("HF_TOKEN environment variable is missing")

            logger.info("Configuration loaded successfully.")

        except FileNotFoundError:
            logger.exception("Configuration file missing.")
            raise

        except tomli.TOMLDecodeError:
            logger.exception("Invalid TOML format.")
            raise

        except KeyError as e:
            logger.exception(f"Missing configuration key: {e}")
            raise

        except Exception:
            logger.exception("Unexpected configuration error.")
            raise


settings = Settings()