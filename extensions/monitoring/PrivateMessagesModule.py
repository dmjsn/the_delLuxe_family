import discord
from discord.ext import commands
from core import logger

class PrivateMessages(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        logger.info('PrivateMessages Cog loaded')

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot or not isinstance(message.channel, discord.DMChannel):
            return

        logger.info(f"Message from {message.author}: {message.content}")

        if message.content == "id":
            try:
                await message.channel.send(f"Твой id: {message.author.id}")
                logger.info(f"A message has been sent to {message.author}. Id: {message.author.id}")
            except Exception as e:
                logger.error(f"PrivateMessages: {e}")
        else:
            await message.channel.send("Тебе что здесь надо ?")

async def setup(bot):
    await bot.add_cog(PrivateMessages(bot))
