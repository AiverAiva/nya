import discord
# from discord import app_commands
from discord.ext import commands
from discord.ui import Button, View
from discord.commands import Option
import requests
import time
import datetime
import sys
sys.path.append("..")
import utilties.embeds as embeds
import ui.wynncraft as wynncraft
from utilties.multicog import add_to_group

bot = discord.Bot()


class player(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @add_to_group('wynncraft')
    @discord.slash_command(name = "player", description = "Check player stats.")
    async def player(self, ctx, name :Option(str, "The name of the player you want to search for.")):
        pd = requests.get(f"https://api.wynncraft.com/v2/player/{name}/stats").json()
        try:
            data = pd["data"][0]
        except:
            return await ctx.respond(embed=embeds.embedError(f"Unknown player `{name}`"))
    
        button_overall = Button(label="Overall", style=discord.ButtonStyle.blurple, emoji="👥")
        async def overall_callback(interaction):
            await interaction.response.edit_message(embed=wynncraft.overall(data))
        button_overall.callback = overall_callback
    
        button_dungeonandraid = Button(label="Dungeon&Raid", style=discord.ButtonStyle.blurple, emoji="🗝️")
        async def dungeonandraid_callback(interaction):
            await interaction.response.edit_message(embed=wynncraft.dungeonandraid(data))
        button_dungeonandraid.callback = dungeonandraid_callback
    
        view = View(button_overall, button_dungeonandraid)
    
        await ctx.respond(embed=wynncraft.overall(data), view=view)

def setup(bot):
    bot.add_cog(player(bot))