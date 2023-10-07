import discord
from discord.ext import commands, pages
from discord.commands import Option
import time
import sys
sys.path.append("..")
import requests
import utilties.requests as requests
import utilties.embeds as embeds
import utilties.list as list
from utilties.multicog import add_to_group
bot = discord.Bot()

class leaderboard(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def sortByKey(e):
        return e['lastSeen']   

    @add_to_group('wynncraft')
    @discord.slash_command(name = "leaderboard", description = "The leaderboard of wynncraft things.")
    async def leaderboard(self, ctx, option :Option(str, description="Choose the leaderboard you want to check", choices=list.lbList), guild: Option(str, "(Optional) Input a guild name if you want to check a specific guild.", required = False, default='')):
        start_time = time.time()
        # guildData = requests.getGuild(guild)
        await ctx.respond(embed=embeds.embedProcessing())
        # def getGuildName(guild):
        #     r = requests.get(f'http://avicia.ga/api/tag/?tag={guild}').json()
        #     if r == "null":
        #         a = requests.get(f'https://api.wynncraft.com/public_api.php?action=guildStats&command={guild}').json()
        #         if "error" in a:
        #             return ""
        #         else:
        #             return a
        #     elif isinstance(r, str) is False: 
        #         return r[list(r)[0]]
        #     else:
        #         return r
        lbembeds = await embeds.embedGroupLeaderboard(option, guild)
        # if guild != '':
        #     guildName = getGuildName(guild)
        #     if guildName == "":
        #         return await ctx.edit(embed=embeds.embedError(f'The guild `{guild}` is unknown. Please check if there is any uppercase or whether the tag is correct.'))
        #     lbembeds = await embeds.embedGroupLeaderboard(option, guildName)
        # else:
        #     lbembeds = await embeds.embedGroupLeaderboard(option, guild)

        selectMenuOptions = []
        for i in range(len(lbembeds)):
            selectMenuOptions.append(discord.SelectOption(
                        label=f"Range {i*20+1}~{i*20+20}",
                        value=str(i),
                    ))

        selectMenu= discord.ui.Select(
                placeholder="Range",
                options = selectMenuOptions
            ) 
        async def select_callback(interaction):
            await interaction.response.edit_message(embed=lbembeds[int(selectMenu.values[0])])

        selectMenu.callback = select_callback
        view = discord.ui.View()
        view.add_item(selectMenu)
        await ctx.edit(content=f"Query took {time.time()-start_time}s", embed=lbembeds[0], view=view)
        

def setup(bot):
    bot.add_cog(leaderboard(bot))