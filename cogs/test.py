import discord
from discord.ext import commands
from discord.ui import Button, View
from discord.commands import Option
import requests
import time
import datetime
import sys
sys.path.append("..")
import utilties.embeds as embeds
# from utilties import embeds
# import handlers.embeds as embeds

bot = discord.Bot()

class item(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @bot.slash_command(name = "item", description = "check the stats of an item")
    async def item(self, ctx, name :Option(str, "The item name you want to search for.")):
        query = requests.get(f"https://api.wynncraft.com/public_api.php?action=itemDB&search={name}").json()
        items=list(query["items"])

        if len(items) == 0:
            await ctx.respond(embed=embeds.embedError(f"There's no item with `{name}` in its name."))
        elif len(items) >= 10:
            await ctx.respond(embed=embeds.embedError(f"Too many items with `{name}` in its name, try a more accurate name."))
        else:
            li = list(map(lambda x: x["name"], items))
            view=discord.ui.View()
            for item in li:
                # my_button[item] = {}
                # my_button[item]["button"] = 
                view.add_item(Button(label=item, style=discord.ButtonStyle.gray))
                # async def button_callback(interaction):
                #     await interaction.response.send_message(item)
                # my_button[item]["button"].callback=button_callback(item=my_button[item]["name"])
            await ctx.respond(content=li, view=view)

def setup(bot):
    bot.add_cog(item(bot))