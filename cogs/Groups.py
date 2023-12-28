import discord
from discord.ext import commands

bot = discord.Bot()

class Groups(commands.Cog):
    wynncraft = discord.SlashCommandGroup(name="wynncraft")
  
    def __init__(self, bot):
        self.bot = bot

def setup(bot):
    bot.add_cog(Groups(bot))