import discord
import os
# from discord import app_commands
from discord.ext import commands
from discord.commands import Option
from utilties.multicog import add_to_group
from utilties.requests import checkMinecraftName
import utilties.embeds as embeds
import utilties.database as Database
import sys
sys.path.append("..")

bot = discord.Bot()

class unlink(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @add_to_group('wynncraft')
    @discord.slash_command(name = "unlink", description = "unlink your account", pass_context=True)
    async def player(self, ctx):
        query = {"discordid": ctx.author.id}    
        newvalue = {"wynncraft": None}
        await Database.initUserData(ctx.author.id)
        await Database.updateUserData(query, newvalue)
        await ctx.respond(embed=embeds.Success(f"Your Wynncraft account has been successfully unlinked."))

def setup(bot):
    bot.add_cog(unlink(bot))