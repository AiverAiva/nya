import discord
import datetime

import sys
sys.path.append("..")
from utilties import colors, requests, formatter, emoji

def overall(data):
    t=f'Playtime: {round(int(data["meta"]["playtime"])*4.7/60)}hr\nFirst Join: <t:{formatter.getTime(data["meta"]["firstJoin"])}:R>\nLast Seen: <t:{formatter.getTime(data["meta"]["lastJoin"])}:R>\n'
    if data["guild"]["name"] is not None:
        t+=f'Guild: {data["guild"]["name"]} ({data["guild"]["rank"]})\n'
    t+="\n"
    username = data["username"].replace("_", "\_")
    title = username if data["meta"]["tag"]["value"] is None else f'{username} [{data["meta"]["tag"]["value"]}]'
    embed=discord.Embed(
        title=title, 
        color=colors.getWynncraftRankColor(data["meta"]["tag"]["value"]),
        description=t
    )
    embed.set_thumbnail(url=f'https://mc-heads.net/head/{data["username"]}')
    return embed

def dungeonandraid(data):
    username = data["username"].replace("_", "\_")
    title = username if data["meta"]["tag"]["value"] is None else f'{username} [{data["meta"]["tag"]["value"]}]'
    embed=discord.Embed(
        title=title, 
        color=colors.getWynncraftRankColor(data["meta"]["tag"]["value"]),
    )
    embed.set_thumbnail(url=f'https://mc-heads.net/head/{data["username"]}')
    dungeonandraidstats = formatter.wynncraftdungeonnraid(data)
    completedDungeons = "This player haven't completed any dungeon yet." if len(dungeonandraidstats["dungeons"]) == 0 else ""
    embed.add_field(name=f'Dungeons', value=completedDungeons, inline=False)
    for i in dungeonandraidstats["dungeons"]:
        valuet = ""
        if "normal" in dungeonandraidstats["dungeons"][i]: valuet += f'<:normaldungeonkey:1064531252729872456> {dungeonandraidstats["dungeons"][i]["normal"]}'
        if "corrupted" in dungeonandraidstats["dungeons"][i]: valuet += f'<:corrupteddungeonkey:1064531265681895424> {dungeonandraidstats["dungeons"][i]["corrupted"]}'
        embed.add_field(name=f"{emoji.getWynncraftDnREmoji(i)} {i}", value=valuet, inline=True)
    completedRaids = "This player haven't completed any raid yet." if len(dungeonandraidstats["raids"]) == 0 else ""
    embed.add_field(name=f'Raids', value=completedRaids, inline=False)
    for i in dungeonandraidstats["raids"]:
        embed.add_field(name=f"{emoji.getWynncraftDnREmoji(i)} {i}", value=dungeonandraidstats["raids"][i], inline=True)
    return embed