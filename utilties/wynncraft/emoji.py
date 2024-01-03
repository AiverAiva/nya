wynnIcon = "<:wynncraft:1191134022038978590>"

def getWynnDungeonRaidEmoji(name):
    dict = {
        "Decrepit Sewers": "<:DecrepitSewersIconmin:1064502738697850900>", 
        "Infested Pit": "<:InfestedPitIconmin:1064502749833728010>", 
        "Lost Sanctuary": "<:LostSanctuaryIconmin:1064502752551632936>", 
        "Underworld Crypt": "<:UnderworldCryptIconmin:1064502764853542912>", 
        "Sand-Swept Tomb": "<:SandSweptTombIconmin:1064502757182144513>", 
        "Ice Barrows": "<:IceBarrowsIconmin:1064502744586670110>", 
        "Undergrowth Ruins": "<:UndergrowthRuinsIconmin:1064502760973815848>", 
        "Galleon's Graveyard": "<:GalleonsGraveyardIconmin:1064502734180581408>", 
        "Fallen Factory": "<:FallenFactoryIconmin:1064527572601413702>", 
        "Eldritch Outlook": "<:EldritchOutlookIconmin:1064502740568514620>",
        "Nest of the Grootslangs": "<:NestoftheGrootslangsIconmin:1064749754011111474>",
        "Orphion's Nexus of Light": "<:Orphion27sNexusofLightIconmin:1064749758389960745>", 
        "The Canyon Colossus": "<:TheCanyonColossusIconmin:1064749762806562866>", 
        "The Nameless Anomaly": "<:TheNamelessAnomalyIconmin:1064749767894253629>"
    }

    return dict[name]

def getWynnClassIcon(name):
    dict = {
        "SHAMAN": "<:relik:1192159877053825075>",
        "ASSASSIN":"<:dagger:577051297027457036>",
        "MAGE": "<:wand:577055020168511488>",
        "WARRIOR": "<:spear:577054598062276619>",
        "ARCHER": "<:bow:577054598238306314>",

        "SKYSEER": "<:relik:1192159877053825075>",
        "NINJA":"<:dagger:577051297027457036>",
        "DARKWIZARD": "<:wand:577055020168511488>",
        "KNIGHT": "<:spear:577054598062276619>",
        "HUNTER": "<:bow:577054598238306314>"
    }

    return dict[name]

def getWynnProfIcon(name):
    dict = {
        "armouring":"<:armouring:578242781450076160>",
        "cooking":"<:cooking:578242781458333696>" ,
        "jeweling":"<:jeweling:578242781441425422>" ,
        "scribing":"<:scribing:578242781408002058>" ,
        "tailoring":"<:tailoring:578242781378510862>" ,
        "weaponsmithing":"<:weaponsmithing:578242781399744522>" ,
        "woodworking" :"<:woodworking:578242781470785556>" ,
        "alchemism":"<:alchemism:578239155578994689>" ,
        "fishing":"<:fishing:578235365652037633> " ,
        "farming":"<:farming:578235327127355420>" ,
        "mining":"<:mining:577882452287029248>" ,
        "woodcutting":"<:woodcutting:577883376456040489>" 
    } 

    return dict[name]

def getWynnRankTagEmoji(name):
    dict = {
        "VIP": "<:rank_vip_01:1192173664377000099><:rank_vip_02:1192173667539484722>",
        "VIP+":"<:rank_vipplus_01:1192173669611491520><:rank_vipplus_02:1192173673344417822><:rank_vipplus_03:1192173676234281110>",
        "HERO": "<:rank_hero_01:1192173656898555955><:rank_hero_02:1192173659134107738><:rank_hero_03:1192173662242099200>",
        "CHAMPION": "<:rank_champion_01:1192173644399509595><:rank_champion_02:1192173647163568129><:rank_champion_03:1192173649218785342><:rank_champion_04:1192173652393869453><:rank_champion_05:1192173654289682512>",
        "Media": "<:rank_media_01:1192174609278189721><:rank_media_02:1192174612818178209><:rank_media_03:1192174614625919108><:rank_media_04:1192174617226383360>",
        "Item": "<:rank_item_01:1192217026391965756><:rank_item_02:1192217029424468049><:rank_item_03:1192217031177674783>",
        "Moderator": "<:rank_moderator_01:1192175684643197019><:rank_moderator_02:1192175687646322748><:rank_moderator_03:1192175689584087080><:rank_moderator_04:1192175692436230185><:rank_moderator_05:1192175694193623192><:rank_moderator_06:1192175697129656450>",
        "Administrator": "<:rank_admin_01:1192215920391766117><:rank_admin_02:1192215923243896925><:rank_admin_03:1192215924837732485><:rank_admin_04:1192215927501115563>"
    } 

    return dict[name]