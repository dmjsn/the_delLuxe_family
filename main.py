import asyncio
from config import settings
from core import bot

async def main():
    try:
        await bot.start(settings.TOKEN)
    except KeyboardInterrupt:
        await bot.stop()

if __name__ == '__main__':
    asyncio.run(main())
