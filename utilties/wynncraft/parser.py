import datetime
from . import lists

def getTime(timestamp):
    element = datetime.datetime.strptime(timestamp,"%Y-%m-%dT%H:%M:%S.%fZ")
    return round(element.timestamp())+8*3600

def getRankTag(data):
    return data["meta"]["tag"]["value"] if data['rank'] == "Player" else data['rank']

def getUnformattedClass(name):
    list = {
        #normal class
        "ASSASSIN": "Assassin",
        "MAGE": "Mage",
        "ARCHER": "Archer",
        "SHAMAN": "Shaman",
        "WARRIOR": "Warrior",
        #ranked class
        "DARKWIZARD": "Dark Wizard",
        "HUNTER": "Hunter",
        "KNIGHT": "Knight",
        "NINJA": "Ninja",
        "SKYSEER": "Skyseer"
    }
    return list[name]

def parseDungeonRaidData(data, id=None):
    stats = {
        "dungeons": {},
        "raids": {}
    }
    new_dictionary = {
        "dungeons": {},
        "raids": {}
    }

    def iterate():
        for dungeon in data["characters"][character]["dungeons"]["list"]:
            try:
                stats["dungeons"][dungeon["name"]] += dungeon["completed"]
            except:
                stats["dungeons"][dungeon["name"]] = dungeon["completed"]
        for raid in data["characters"][character]["raids"]["list"]:
            try:
                stats["raids"][raid["name"]] += raid["completed"]
            except:
                stats["raids"][raid["name"]] = raid["completed"]

    if id is not None:
        iterate()
    else:
        for character in data["characters"]:
            iterate()
        

    for i in lists.lbList:
        if i in stats["dungeons"]:
            if i.startswith("Corrupted"):
                if i.lstrip("Corrupted ") not in new_dictionary["dungeons"]: new_dictionary["dungeons"][i.lstrip("Corrupted ")] = {}
                new_dictionary["dungeons"][i.lstrip("Corrupted ")]["corrupted"] = stats["dungeons"][i]
            else:
                if i not in new_dictionary["dungeons"]: new_dictionary["dungeons"][i] = {}
                new_dictionary["dungeons"][i]["normal"] = stats["dungeons"][i]
        if i in stats["raids"]:
            new_dictionary["raids"][i] = stats["raids"][i]
    return new_dictionary

