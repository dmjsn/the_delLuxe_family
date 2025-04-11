import os
from dotenv import load_dotenv
from typing import List

load_dotenv()

class Settings:
    """Настройки бота"""

    TOKEN: str = os.getenv("BOT_TOKEN")
    """Токен бота"""

    PREFIXES: List[str] = ["!", "?"]
    """Префиксы для команд бота"""

    DEBUG: bool = os.getenv("DEBUG", "False") == "True"
    """Флаг для переключения в режим debug"""

    EXTENSIONS: List[str] = [

    ]
    """Список модулей (Cogs) для автоматической загрузки"""

    @property
    def intents(self) -> dict:
        """Настройки Discord Intents (разрешений бота)"""
        return {
            "messages": True,
            "guilds": True,
            "members": True,
            "reactions": True,
            "voice_states": True
        }
