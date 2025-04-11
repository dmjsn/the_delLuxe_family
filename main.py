import asyncio
from config import settings
from core import bot
from core import logging

async def main():
    try:
        logging.info('Launching the bot')
        await bot.start(settings.TOKEN)
    except KeyboardInterrupt:
        logging.info('Failed to launch the bot')
        await bot.stop()

if __name__ == '__main__':
    asyncio.run(main())
