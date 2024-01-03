import discord
import datetime
import sys
from . import emoji, lists, parser, colors
sys.path.append("..")
from utilties import requests

def defaultPlayerEmbed(data):
    username = data["username"].replace("_", "\_")
    rankTag = parser.getRankTag(data)
    title = username if rankTag is None else f'{username} {emoji.getWynnRankTagEmoji(rankTag)}'
    embed=discord.Embed(
        title=title, 
        color=colors.getWynncraftRankColor(rankTag),
    )
    return embed

def overall(data):
    t=f'Playtime: {round(int(data["meta"]["playtime"])*4.7/60)}hr\nFirst Join: <t:{parser.getTime(data["meta"]["firstJoin"])}:R>\nLast Seen: <t:{parser.getTime(data["meta"]["lastJoin"])}:R>\n'
    if data["guild"]["name"] is not None:
        t+=f'Guild: {data["guild"]["name"]} ({data["guild"]["rank"]})\n'
    t+="\n"
    embed=defaultPlayerEmbed(data)
    embed.description = t
    embed.set_thumbnail(url=f'https://mc-heads.net/head/{data["username"]}')
    return embed

def dungeonandraid(data):
    embed=defaultPlayerEmbed(data)
    embed.set_thumbnail(url=f'https://mc-heads.net/head/{data["username"]}')
    dungeonandraidstats = parser.parseDungeonRaidData(data)
    completedDungeons = "This player haven't completed any dungeon yet." if len(dungeonandraidstats["dungeons"]) == 0 else ""
    embed.add_field(name=f'Dungeons', value=completedDungeons, inline=False)
    for i in dungeonandraidstats["dungeons"]:
        valuet = ""
        if "normal" in dungeonandraidstats["dungeons"][i]: valuet += f'<:normaldungeonkey:1064531252729872456> {dungeonandraidstats["dungeons"][i]["normal"]}'
        if "corrupted" in dungeonandraidstats["dungeons"][i]: valuet += f'<:corrupteddungeonkey:1064531265681895424> {dungeonandraidstats["dungeons"][i]["corrupted"]}'
        embed.add_field(name=f"{emoji.getWynnDungeonRaidEmoji(i)} {i}", value=valuet, inline=True)
    completedRaids = "This player haven't completed any raid yet." if len(dungeonandraidstats["raids"]) == 0 else ""
    embed.add_field(name=f'Raids', value=completedRaids, inline=False)
    for i in dungeonandraidstats["raids"]:
        embed.add_field(name=f"{emoji.getWynnDungeonRaidEmoji(i)} {i}", value=dungeonandraidstats["raids"][i], inline=True)
    return embed

def classOverlay(data, id):
    embed=defaultPlayerEmbed(data)
    embed.description = parser.getUnformattedClass(data['characters'][id]['type']) + id  
    embed.set_thumbnail(url=f'https://mc-heads.net/head/{data["username"]}')

    professions = ""
    # data['characters'][id]['professions']['combat']
    for i in lists.profList:
        if i == 'combat': continue
        professions += f"{emoji.getWynnProfIcon(i)} **{data['characters'][id]['professions'][i]['level']}** {i.capitalize()}  \n"
    embed.add_field(name="Professions", value=professions, inline=True)

    dungeonandraidstats = parser.parseDungeonRaidData(data, id)
    completedDungeons = "This player haven't completed any dungeon yet." if len(dungeonandraidstats["dungeons"]) == 0 else ""
    embed.add_field(name=f'Dungeons', value=completedDungeons, inline=False)
    for i in dungeonandraidstats["dungeons"]:
        valuet = ""
        if "normal" in dungeonandraidstats["dungeons"][i]: valuet += f'<:normaldungeonkey:1064531252729872456> {dungeonandraidstats["dungeons"][i]["normal"]}'
        if "corrupted" in dungeonandraidstats["dungeons"][i]: valuet += f'<:corrupteddungeonkey:1064531265681895424> {dungeonandraidstats["dungeons"][i]["corrupted"]}'
        completedDungeons += f"{emoji.getWynnDungeonRaidEmoji(i)} **{i}** " + valuet
        
    embed.add_field(name=f"", value=valuet, inline=True)
    completedRaids = "This player haven't completed any raid yet." if len(dungeonandraidstats["raids"]) == 0 else ""
    embed.add_field(name=f'Raids', value=completedRaids, inline=False)
    for i in dungeonandraidstats["raids"]:
        embed.add_field(name=f"{emoji.getWynnDungeonRaidEmoji(i)} {i}", value=dungeonandraidstats["raids"][i], inline=True)

    return embed


def classSelectMenu(data):
    options = []
    for i in data['characters']:
        options.append(discord.SelectOption(
            label=parser.getUnformattedClass(data['characters'][i]['type']),
            value=i,
            description=str(data['characters'][i]['level']),
            emoji=emoji.getWynnClassIcon(data['characters'][i]['type'])
        ))
    
    selectMenu=discord.ui.Select(
        placeholder="Click here to select a class",
        options = options
    ) 
    return selectMenu