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
from utilties.wynncraft import ui, colors

from utilties.multicog import add_to_group
from utilties.database import getUserData

bot = discord.Bot()

class player(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @add_to_group('wynncraft')
    @discord.slash_command(name = "player", description = "Check player stats.")
    async def player(self, ctx, name :Option(str, "The name of the player you want to search for.", required=False)):
        if name is None:
            userdata = await getUserData(ctx.author.id)
            dbname = userdata['wynncraft']
            if dbname is None:
                return await ctx.respond(embed=embeds.Error(f"You don't have an account connected to the bot, use </wynncraft link:1160063178907062342> to link"))
            else:
                name = dbname
        pd = requests.get(f"https://api.wynncraft.com/v2/player/{name}/stats").json()
        try:
            data = pd["data"][0]
        except:
            return await ctx.respond(embed=embeds.Error(f"Unknown player `{name}`"))
    
        button_overall = Button(label="Overall", style=discord.ButtonStyle.blurple, emoji="👥")
        async def overall_callback(interaction):
            await interaction.response.edit_message(embed=ui.overall(data), view=view)
        button_overall.callback = overall_callback
    
        button_dungeonandraid = Button(label="Dungeon&Raid", style=discord.ButtonStyle.blurple, emoji="🗝️")
        async def dungeonandraid_callback(interaction):
            await interaction.response.edit_message(embed=ui.dungeonandraid(data), view=view)
        button_dungeonandraid.callback = dungeonandraid_callback

        button_classes = Button(label="Classes", style=discord.ButtonStyle.blurple, emoji="🗝️")
        async def classes_callback(interaction):
            chooseClass = ui.defaultPlayerEmbed(data)
            chooseClass.description = "Choose a class to conitnue:",
            await interaction.response.edit_message(embed=chooseClass, view=selectMenuview)
        button_classes.callback = classes_callback
        
        async def select_callback(interaction):
            await interaction.response.edit_message(embed=ui.classOverlay(data, selectMenu.values[0]))

        selectMenu = ui.classSelectMenu(data)
        selectMenu.callback = select_callback
        view = View(button_overall, button_dungeonandraid, button_classes)
        selectMenuview = View(button_overall, button_dungeonandraid, button_classes, selectMenu)
        await ctx.respond(embed=ui.overall(data), view=view)

def setup(bot):
    bot.add_cog(player(bot))