import datetime


def getTime(timestamp):
    element = datetime.datetime.strptime(timestamp,"%Y-%m-%dT%H:%M:%S.%fZ")
    return round(element.timestamp())+8*3600

def wynncraftdungeonnraid(data):
    list = [
        "Decrepit Sewers", "Infested Pit", "Lost Sanctuary", "Underworld Crypt", "Sand-Swept Tomb", "Ice Barrows", "Undergrowth Ruins", "Galleon's Graveyard", "Fallen Factory", "Eldritch Outlook",
        "Corrupted Decrepit Sewers", "Corrupted Infested Pit", "Corrupted Lost Sanctuary", "Corrupted Underworld Crypt", "Corrupted Sand-Swept Tomb", "Corrupted Ice Barrows", "Corrupted Undergrowth Ruins", "Corrupted Galleon's Graveyard", 
        "Nest of the Grootslangs", "Orphion's Nexus of Light", "The Canyon Colossus", "The Nameless Anomaly"
    ]
    stats = {
        "dungeons": {},
        "raids": {}
    }
    new_dictionary = {
        "dungeons": {},
        "raids": {}
    }
    for character in data["characters"]:
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

    for i in list:
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