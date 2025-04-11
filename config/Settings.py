import os
from dotenv import load_dotenv
from typing import List, Dict

load_dotenv()

class Settings:
    """Настройки бота"""

    TOKEN: str = os.getenv("BOT_TOKEN")

    PREFIXES: List[str] = ["!", "?"]

    DEBUG: bool = os.getenv("DEBUG", "False") == "True"

    EXTENSIONS: List[str] = [

    ]

    INTENTS: Dict[str, bool] = {
        "messages": True,
        "guilds": True,
        "members": True,
        "voice_states": True
    }
