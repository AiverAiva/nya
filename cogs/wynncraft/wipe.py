import discord
from discord.ext import commands, pages
from discord.commands import Option
import requests
import time
import sys
sys.path.append("..")
import utilties.embeds as embeds
from utilties.multicog import add_to_group

bot = discord.Bot()

class wipe(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
      
    @add_to_group('wynncraft')
    @discord.slash_command(name = "wipe", description = "Checking the online stats of guilds that owns over 5 territories.")
    @commands.cooldown(1, 30, commands.BucketType.user)
    async def wipe(self, ctx):
        def getWipeList():
            r = requests.get("https://api.wynncraft.com/public_api.php?action=statsLeaderboard&type=guild&timeframe=alltime").json()
            a = requests.get("https://api.wynncraft.com/public_api.php?action=onlinePlayers").json()
            onlinePlayers = []
            guilds = []
            detailedGuilds = {}
            for i in r["data"]:
                if i["territories"] > 1:
                    guilds.append(i["name"])
                else:
                    continue
            for e in a:
                for player in a[e]:
                    onlinePlayers.append(player)
            for i in guilds:
                c = requests.get(f'https://api.wynncraft.com/public_api.php?action=guildStats&command={i}').json()
                gstats = {
                    "name": i,
                    "territories": c["territories"],
                    "onlineMember": 0,
                    "onlineChiefOrStrategist": 0
                }
                for n in c["members"]:
                    try: 
                        onlinePlayers.index(n["name"])
                        gstats["onlineMember"] += 1
                        if n["rank"] == "STRATEGIST":
                            gstats["onlineChiefOrStrategist"] += 1
                        if n["rank"] == "CHIEF":
                            gstats["onlineChiefOrStrategist"] += 1
                    except:
                        pass
                detailedGuilds[i] = gstats
            return detailedGuilds
        start_time = time.time()
        await ctx.respond(embed=embeds.embedProcessing())
        thelist = getWipeList()
        thenewlist = []
        for i in thelist:
            thenewlist.append(thelist[i])

        selectMenu= discord.ui.Select(
                placeholder="Sort by?",
                options = [ 
                    discord.SelectOption(
                        label="Territories",
                        value="territories",
                        description="Sort by the number of territories owned."
                    ),
                    discord.SelectOption(
                        label="Online Member Count",
                        value="onlineMember",
                        description="Sort by the number of online members."
                    ),
                    discord.SelectOption(
                        label="Online Chief/Staff Count",
                        value="onlineChiefOrStrategist",
                        description="Sort by the number online Chief/Strategist."
                    )
                ]
            ) 
        
        def sort(q):
            t="```\n" + '{:>20}'.format("Guild Name") + " ┃" + '{:^4}'.format("T") + "┃" + '{:^4}'.format("OM") + "┃" + '{:^5}'.format(" OC/S") + "\n━━━━━━━━━━━━━━━━━━━━━╋━━━━╋━━━━╋━━━━━━\n"
            def sortByKey(e):
                return e[q]   
            thenewlist.sort(key=sortByKey, reverse=True)
            for i in thenewlist:
                t += '{:>20}'.format(f"{i['name']}") + " ┃" + '{:^4}'.format(i['territories'])  + "┃" + '{:^4}'.format(i["onlineMember"]) + "┃" + '{:^5}'.format(i["onlineChiefOrStrategist"]) + "\n"
            t+="\n(T=Territories, OM=Member, OC/S=Chief/Strategist)```"
            return t

        def getembed(a):
            embed = discord.Embed(
                title="The stats of top guilds",
                description=sort(a)
            )
            return embed

        async def select_callback(interaction):
            await interaction.response.edit_message(embed=getembed(selectMenu.values[0]))

        selectMenu.callback = select_callback
        view = discord.ui.View()
        view.add_item(selectMenu)
        
        await ctx.edit(content=f"Query took {time.time()-start_time}s", embed=getembed("territories"), view=view)
        
    @wipe.error
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.respond(f'This command is on cooldown, you can use it in {round(error.retry_after, 2)}s')

def setup(bot):
    bot.add_cog(wipe(bot))