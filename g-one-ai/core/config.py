import os
from pathlib import Path

from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parents[1]
load_dotenv(BASE_DIR / ".env")


def _env_int(name, default):
    try:
        return int(os.getenv(name, default))
    except (TypeError, ValueError):
        return default


OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4.1-mini")
ASSISTANT_NAME = os.getenv("ASSISTANT_NAME", "G-ONE")
VOICE_RATE = _env_int("VOICE_RATE", 170)
DATABASE_PATH = BASE_DIR / "g_one_memory.db"
