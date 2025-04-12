import asyncio
import logging
from config import settings
from core import bot
from core import logger

logging.getLogger('asyncio').setLevel(logging.CRITICAL)
logging.getLogger('discord').setLevel(logging.CRITICAL)

async def main():
    try:
        logger.info('Launching the bot')
        await bot.start(settings.TOKEN)
    except KeyboardInterrupt:
        logger.info('Shutting down the bot')
        await bot.stop()

if __name__ == '__main__':
    asyncio.run(main())
