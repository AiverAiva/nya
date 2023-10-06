main = 0x639c9c
error = 0xfc8d8d
joined = 0xBFFFC6
left = 0xFF7A8A 

embedbg = 0x2F3136
blurple = 0x5865f2

def getWynncraftRankColor(input):
    dict = {
        None: 0xAAAAAA,
        "VIP": 0x55ff55,
        "VIP+": 0x55ffff,
        "HERO": 0xbd5fdd,
        "CHAMPION": 0xf8ac38
    }
    return dict[input]