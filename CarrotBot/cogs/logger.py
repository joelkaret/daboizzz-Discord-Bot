import discord
from discord.ext import commands
from discord.utils import get

class logger(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    #Check
    async def is_me(ctx):
        return ctx.author.id == 506884005195677696 #MyID

    @commands.Cog.listener()
    async def on_message(self, msg):
        if msg.channel.name == "officer-chat":
            await self.log_officer_Chat(msg)
        elif msg.channel.name == "core-members":
            await self.log_officer_Chat(msg)
        else:
            await self.log_all(msg)
        self.bot.process_commands(msg)



    async def log_officer_chat(self, msg):
        loggerguild = 940647396461912134
        log_channel = discord.utils.get(loggerguild.channels, name="officer-chat")
        try:
            await log_channel.send(f"*{msg.content}*, sent by **{msg.author.nick}** who is also **{msg.author}")
        except Exception:
            print("'logs' channel not found, or bot missing permissions")

    async def log_core_members(self, msg):
        loggerguild = 940647396461912134
        log_channel = discord.utils.get(loggerguild.channels, name="core-members")
        try:
            await log_channel.send(f"*{msg.content}*, sent by **{msg.author.nick}** who is also **{msg.author}")
        except Exception:
            print("'logs' channel not found, or bot missing permissions")

    async def log_all(self, msg):
        loggerguild = 940647396461912134
        log_channel = discord.utils.get(loggerguild.channels, name="all")
        try:
            await log_channel.send(f"*{msg.content}*, sent by **{msg.author.nick}** who is also **{msg.author}")
        except Exception:
            print("'logs' channel not found, or bot missing permissions")
    
def setup(bot):
    bot.add_cog(logger(bot))