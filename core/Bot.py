import discord
from discord.ext import commands
from config import settings

class Bot(commands.Bot):
    """Ядро бота"""

    def __init__(self):
        super().__init__(
            command_prefix=settings.PREFIXES,
            intents=discord.Intents(**settings.INTENTS),
            case_insensitive=True
        )

    async def setup_hook(self):
        """Инициализация при старте"""
        await self.load_extensions()

    async def load_extensions(self):
        """Загрузка всех модулей"""
        for ext in settings.EXTENSIONS:
            await self.load_extension(f"extensions.{ext}")
