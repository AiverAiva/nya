def getWynncraftRankColor(input):
    dict = {
        None: 0xAAAAAA,
        "VIP": 0x44aa33,
        "VIP+": 0x446dbb,
        "HERO": 0xa344aa,
        "CHAMPION": 0xffaa00,
        "Media": 0xbf3399,
        "Item": 0x00aaaa,
        "Moderator": 0xff6a00,
        "Administrator": 0xd11111
    }
    return dict[input]