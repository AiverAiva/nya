import discord
from . import colors, requests

def progress_bar(percent: int) -> str:
    bar = ""

    for _ in range(round(max(min(percent, 100), 0) / 10)):
        bar += "🟨"

    return bar.ljust(10, "⬛")

async def embedGroupGuildInfo(guildData):
    onlinePlayer = await requests.getGuildOnlinePlayer(guildData)
    t = "```\n"
    if not onlinePlayer:
        t+="No player online"
    else:
        for i in onlinePlayer:
            t += '{:<18}'.format(i["name"]) + '{:^11}'.format(i["rank"]) + '{:>5}'.format(i["server"]) + "\n"
    t += "```"
    embedGroup = [
        discord.Embed(
            title=f'{guildData["name"]} [{guildData["prefix"]}]',
            description=f'> **Level** {guildData["level"]} | {guildData["xp"]}%\n``` 0 {progress_bar(guildData["xp"])} 100 ```\n```ml\n\nMembers: {len(guildData["members"])} (Online: {len(onlinePlayer)})\nCreated: {guildData["createdFriendly"]}\nTerritories: {guildData["territories"]}```',
            color=colors.embedbg
        ),
        discord.Embed(
            title=f'{guildData["name"]} [{guildData["prefix"]}]',
            description=t, 
            color=colors.embedbg
        )
    ]
    return embedGroup

async def embedGroupInactiveList(guildData):
    embedGroup = []

    inactivePlayer = await requests.getInactivePlayer(guildData)
    composite_list = [inactivePlayer[x:x+20] for x in range(0, len(inactivePlayer),20)]

    for i in composite_list:
        t = ""
        for e in i:
            name = (e['name']).replace("_", "\_")
            if e['lastSeen'] == 0:
                t += f'{name} This is an unknown player.\n'
            else: 
                t += f'{name} <t:{e["lastSeen"]}:R>\n'
        embedGroup.append(t)

    return embedGroup

async def embedGroupLeaderboard(option, guild):
    embedGroup = []
    c=1
    leaderboard = await requests.getLeaderboard(option, guild)
    composite_list = [leaderboard[x:x+20] for x in range(0, len(leaderboard),20)]

    for i in composite_list:
        t = "```\n"
        for e in i:  
            t += '{:<4}'.format(f"{c}.") + '{:^20}'.format(e["name"]) + '{:>7}'.format("{:,}".format(int(e[option]))) + "\n"
            c+=1
        t += "```"
        title=f"The leaderbord of `{option}`"
        if guild != "":
            title+=f" in `{guild}`"
        embedGroup.append(discord.Embed(
            title=title, 
            description=t
        ))

    return embedGroup

def embedProcessing():
    embed=discord.Embed(
        description=f"Processing the the information...", 
        color=colors.main
    )
    return embed

def embedProgressBar():
    embed=discord.Embed(
        title="Progress", 
        color=colors.main
    )
    embed.set_image(url="attachment://image.png")
    return embed

def embedError(text):
    embed=discord.Embed(
        description=text,
        color=colors.error
    )
    return embed