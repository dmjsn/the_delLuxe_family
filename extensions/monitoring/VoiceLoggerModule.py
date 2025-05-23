import discord
from discord.ext import commands
from core import logger

class VoiceLogger(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.monitoredChannels = [1360660216391274671] #отслеживаемый канал
        self.validMember = [471397000236105739, 734396325713412136]
        logger.info('VoiceLogger Cog loaded')

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        logger.info(f"{member} joins the {after.channel.id} channel")
        if after.channel and after.channel.id in self.monitoredChannels:
            if not member.id in self.validMember:
                try:
                    logger.info(f"{member} was disconnected from the {after.channel.name} channel")
                    await member.move_to(None)
                except discord.Forbidden:
                    logger.error('VoiceLogger: Insufficient permissions to move the user to another channel')
                except Exception as e:
                    logger.error(f'VoiceLogger: {e}')

async def setup(bot):
    await bot.add_cog(VoiceLogger(bot))
