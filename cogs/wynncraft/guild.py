import discord
from discord.ext import commands, pages
from discord.commands import Option
import time
import sys
import aiohttp
sys.path.append("..")
import utilties.requests as requests
import utilties.embeds as embeds
from utilties.multicog import add_to_group

bot = discord.Bot()

class guild(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def sortByKey(e):
        return e['lastSeen']       
                  
    @add_to_group('wynncraft')
    @discord.slash_command(name = "guild", description = "Check the guild infomation.")
    async def guild(self, ctx: discord.ApplicationContext, guild :Option(str, "The name or prefix of the guild.")):
        start_time = time.time()
        # guildData = await 
        guildData = await requests.getGuild(guild)
        
        if guildData == "":
            return await ctx.respond(embed=embeds.embedError(f'The guild `{guild}` is unknown. Please check if there is any uppercase or whether the tag is correct.'))

        page_groups = [
            pages.PageGroup(
                pages=await embeds.embedGroupGuildInfo(guildData), 
                label="Basic Guild Infomation",
                description="This tab shows the basic infomation of a guild.",
                loop_pages=True
            )
        ]
        inactivePlayer = await requests.getInactivePlayer(guildData)
        if inactivePlayer is not None:
            page_groups.append(
                pages.PageGroup(
                    pages=await embeds.embedGroupInactiveList(guildData),
                    label="Guild Inactive Player",
                    description="List players from longest last seen to lastest.",
                    loop_pages=True
                )
                #pages.PageGroup(
                #    pages=embeds.embedGroupInactiveList(guildData),
                #    label="Member History",
                #    description="Show the players who joined and left",
                #    loop_pages=True
                #),
                # pages.PageGroup(
                #     pages=embeds.embedGroupInactiveList(guildData),
                #     label="Guild Inactive Player",
                #     description="List players from longest last seen to lastest.",
                #     loop_pages=True
                # )
            )
        paginator = pages.Paginator(pages=page_groups, show_menu=True, loop_pages=True, menu_placeholder="Click here to switch tab")
        await paginator.respond(ctx.interaction, ephemeral=False)
        await ctx.send(content=f"Query took {time.time()-start_time}s")

def setup(bot):
    bot.add_cog(guild(bot))