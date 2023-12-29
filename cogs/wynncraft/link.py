import discord
import os
# from discord import app_commands
from discord.ext import commands
from discord.commands import Option
from utilties.multicog import add_to_group
from utilties.requests import checkMinecraftName
import utilties.database as Database
import sys
sys.path.append("..")

bot = discord.Bot()

class link(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @add_to_group('wynncraft')
    @discord.slash_command(name = "link", description = "link your wynncraft account to discord", pass_context=True)
    async def player(self, ctx, name :Option(str, "the name u want to link for", required=True)):
        
        checked = checkMinecraftName(name)

        if checked is None:
            await ctx.respond(content="please input a valid minecraft username")
        else:
            query = {"discordid": ctx.author.id}    
            newvalue = {"wynncraftName": checked}
            Database.updateUserData(query, newvalue)
            await ctx.respond(content="updated")

def setup(bot):
    bot.add_cog(link(bot))