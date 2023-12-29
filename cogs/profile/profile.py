import discord
import os
from discord.ext import commands
from discord.commands import Option
import sys
import utilties.database as Database
sys.path.append("..")

bot = discord.Bot()

class profile(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @discord.slash_command(name = "profile", description = "show the profile", pass_context=True)
    async def player(self, ctx):
        profile = Database.getUserData(ctx.author.id)
        await ctx.respond(content=profile)

def setup(bot):
    bot.add_cog(profile(bot))