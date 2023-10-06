import requests
import sys
# sys.path.append("..")
# import modules.embeds as embeds

def getGuild(guild):
    r = requests.get(f'http://avicia.ga/api/tag/?tag={guild}').json()
    if r == "null":
        a = requests.get(f'https://api.wynncraft.com/public_api.php?action=guildStats&command={guild}').json()
        if "error" in a:
            return ""
        else:
            return a
    elif isinstance(r, str) is False: 
        return requests.get(f'https://api.wynncraft.com/public_api.php?action=guildStats&command={r[list(r)[0]]}').json()
    else:
        return requests.get(f'https://api.wynncraft.com/public_api.php?action=guildStats&command={r}').json()

def getGuildOnlinePlayer(guildData):
    r = requests.get("https://api.wynncraft.com/public_api.php?action=onlinePlayers").json()
    gmembers = []
    options = {"OWNER": 1, "CHIEF": 2, "STRATEGIST": 3, "CAPTAIN": 4, "RECRUITER": 5, "RECRUIT": 6}

    def sortByKey(e):
        if e['rank'] in options:
            a = options[e['rank']]
        return a

    for e in r:
        for i in guildData["members"]:
            try:
                list(r[e]).index(i["name"])
                gmembers.append({'name': i["name"], 'rank': i["rank"], 'server': e})
            except:
                pass

    gmembers.sort(key=sortByKey)
    return gmembers

def getInactivePlayer(guildData):
    def sortByKey(e):
        return e['lastSeen']

    players= []
    try:
        gd = requests.get(f'https://raw.githubusercontent.com/AiverAiva/wynncraft-data/master/guilds/{guildData["name"]}.json').json()
        for i in gd["members"]:
            players.append({'name': i, 'lastSeen': gd["members"][i]["lastSeen"]})
        players.sort(key=sortByKey)
        return players
        
    except:
        return

def getLeaderboard(option, guild):
    def sortByKey(e):
            return e[option]
    leaderboard = []
    r = requests.get("https://raw.githubusercontent.com/AiverAiva/wynncraft-data/master/datafiles/playerdata.json").json()
    for i in r:
        try:
            if guild != "":
                if r[i]["guild"]["name"] == guild:
                    leaderboard.append({"name": i, option: r[i]["stats"][option]})
            else:
                leaderboard.append({"name": i, option: r[i]["stats"][option]})
        except:
            pass
    leaderboard.sort(key=sortByKey, reverse=True)
    leaderboard = leaderboard[:100]
    return leaderboard
    