import aiohttp
import sys
import json
# sys.path.append("..")
# import modules.embeds as embeds

async def fetch_data(url):
    async with aiohttp.ClientSession() as session:
      headers = {'Accept': 'application/json'}
      async with session.get(url, headers=headers) as response:
          if response.status == 200:
              return await response.json()
              # Process the JSON data
          else:
              print(f'Error: {response.status}')
              return None

async def fetch_raw_data(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                data = await response.text()
                return json.loads(data)
            else:
                print(f'Error: {response.status}')
                return None
                  
async def getGuild(guild):
  r = await fetch_raw_data(f'https://api.weikuwu.me/wynncraft/guildName/{guild}')
  if 'error' in r:
    return ""
  else:
    return await fetch_data(f'https://api.wynncraft.com/public_api.php?action=guildStats&command={r["guildName"]}')
    

async def getGuildOnlinePlayer(guildData):
    r = await fetch_data("https://api.wynncraft.com/public_api.php?action=onlinePlayers")
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

async def getInactivePlayer(guildData):
    def sortByKey(e):
        return e['lastSeen']

    players= []
    try:
        gd = await fetch_raw_data(f'https://raw.githubusercontent.com/AiverAiva/wynncraft-data/master/guilds/{guildData["name"]}.json')
        for i in gd["members"]:
            players.append({'name': i, 'lastSeen': gd["members"][i]["lastSeen"]})
        players.sort(key=sortByKey)
        return players
        
    except:
        return

async def getLeaderboard(option, guild):
    def sortByKey(e):
            return e[option]
    leaderboard = []
    r = await fetch_raw_data("https://raw.githubusercontent.com/AiverAiva/wynncraft-data/master/datafiles/playerdata.json")
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
    