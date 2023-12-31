import discord
import os
from discord.ext import commands
from discord.commands import Option
import sys
import utilties.database as Database
import utilties.emoji as emoji
sys.path.append("..")

bot = discord.Bot()

class profile(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @discord.slash_command(name = "profile", description = "show the profile", pass_context=True)
    async def player(self, ctx):
        
        profile = await Database.getUserData(ctx.author.id)
        embed = discord.Embed(
            title=f'{ctx.author.display_name}\'s Profile',
            
            # description=f''
            # color=
        )
        embed.set_thumbnail(url=ctx.author.display_avatar.url)
        # embed.set_image(ctx.author.banner)
        embed.add_field(name=f"**Linked Accounts**", value=f"{emoji.wynnIcon} Wynncraft `{profile['wynncraft']}`")
        await ctx.respond(embed=embed)
        
def setup(bot):
    bot.add_cog(profile(bot))