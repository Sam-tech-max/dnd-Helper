import Equipment.Armor as A
import Equipment.Item as I
import Equipment.Tool as T
import Equipment.Weapon as W
from typing import List


def getBackpack(background: str) -> List[I.Item]:
    background = background.lower()
    if(background == "acolyte"):
        return getAcolyteBackpack()
    elif(background == "charlatan"):
        return getCharlatanBackpack()
    elif(background == "criminal"):
        return getCriminalBackpack()
    elif(background == "entertainer"):
        return getEntertainerBackpack()
    elif(background == "folk hero"):
        return getFolkHeroBackpack()
    elif(background == "guild artisan"):
        return getGuildArtisanBackpack()
    elif(background == "hermit"):
        return getHermitBackpack()
    elif(background == "noble"):
        return getNobleBackpack()
    elif(background == "outlander"):
        return getOutlanderBackpack()
    elif(background == "sage"):
        return getSageBackpack()
    elif(background == "sailor"):
        return getSailorBackpack()
    elif(background == "soldier"):
        return getSoldierBackpack()
    elif(background == "urchin"):
        return getUrchinBackpack()
    else:
        return getAcolyteBackpack()


def choosePrayerBookOrPrayerWheel() -> I.Item:
    print("Choose between a Prayer Book or Prayer Wheel: ")
    print("Enter 1: Prayer Book")
    print("Enter 2: Prayer Wheel")
    prayer = input()
    if(prayer == "1"):
        return I.Item("prayer book", "generic", 0, "gp")
    elif(prayer == "2"):
        return I.Item("prayer wheel", "generic", 0, "gp")
    else:
        print("That is not a valid choice.")
        return choosePrayerBookOrPrayerWheel()


def getAcolyteBackpack() -> List[I.Item]:
    holySymbol = T.chooseHolySymbol()
    prayer = choosePrayerBookOrPrayerWheel()
    incense = I.Item("incense", "generic", 0, "gp", 5)
    vestments = T.Tool("vestments", "generic", 0, "gp", 0, 1)
    clothes = T.Tool("clothes, common", "generic", 5, "sp", 3, 1)
    pouch = T.Tool("pouch", "generic", 5, "sp", 1, 1)
    money = I.Item("money", "money", 15, "gp", 1)
    return [holySymbol, prayer, incense, vestments, clothes, pouch,
            money]


def getCharlatanBackpack() -> List[I.Item]:
    fineClothes = T.Tool("clothes, fine", "generic", 15, "gp", 6, 1)
    disguiseKit = T.Tool("disguise kit", "generic", 25, "gp", 3, 1)
    conTool = T.chooseConTool()
    pouch = T.Tool("pouch", "generic", 5, "sp", 1, 1)
    money = I.Item("money", "money", 15, "gp", 1)
    return [fineClothes, disguiseKit, conTool, pouch, money]


def getCriminalBackpack() -> List[I.Item]:
    crowbar = T.Tool("crowbar", "generic", 2, "gp", 5, 1)
    commonClothes = T.Tool("dark common clothes with a hood",
                           "generic", 5, "sp", 3, 1)
    pouch = T.Tool("pouch", "generic", 5, "sp", 1, 1)
    money = I.Item("money", "money", 15, "gp", 1)
    return [crowbar, commonClothes, pouch, money]

def getEntertainerBackpack() -> List[I.Item]:
    musIns = T.chooseMusicalInstruments()
    trinket = I.chooseTrinket()
    costume = T.Tool("clothes, costume", "generic", 5, "gp", 4, 1)
    pouch = T.Tool("pouch", "generic", 5, "sp", 1, 1)
    money = I.Item("money", "money", 15, "gp", 1)
    return [musIns, trinket, costume, pouch, money]


def getFolkHeroBackpack() -> List[I.Item]:
    artTool = T.chooseArtisanTool()
    shovel = T.Tool("shovel", "generic", 2, "gp", 5, 1)
    pot = T.Tool("iron pot", "generic", 2, "gp", 10, 1)
    common = T.Tool("clothes, common", "generic", 5, "sp", 3, 1)
    pouch = T.Tool("pouch", "generic", 5, "sp", 1, 1)
    money = I.Item("money", "money", 10, "gp", 1)
    return [artTool, shovel, pot, common, pouch, money]


def getGuildArtisanBackpack() -> List[I.Item]:
    artTool = T.chooseArtisanTool()
    letter = I.Item("a letter of introduction from your guild", "generic", 0, "gp", 1)
    clothes = T.Tool("clothes, traveler's", "generic", 2, "gp", 4, 1)
    pouch = T.Tool("pouch", "generic", 5, "sp", 1, 1)
    money = I.Item("money", "money", 15, "gp", 1)
    return [artTool, letter, clothes, pouch, money]


def getHermitBackpack() -> List[I.Item]:
    scroll = I.Item("a scroll case stuffed full of notes from your studies or prayers", "generic", 0, "gp", 1)
    blanket = T.Tool("winter blanket", "generic", 5, "sp", 3, 1)
    common = T.Tool("clothes, common", "generic", 5, "sp", 3, 1)
    herbKit = T.Tool("herbalism kit", "kit", 5, "gp", 3, 1)
    money = I.Item("money", "money", 5, "gp", 1)
    return [scroll, blanket, common, herbKit, money]


def getNobleBackpack() -> List[I.Item]:
    fine = T.Tool("clothes, fine", "generic", 15, "gp", 6, 1)
    ring = T.Tool("signet ring", "generic", 5, "gp", 0, 1)
    scroll = T.Tool("a scroll of pedigree", "generic", 0, "gp", 0, 1)
    purse = T.Tool("purse", "generic", 5, "sp", 1, 1)
    money = I.Item("money", "money", 25, "gp", 1)
    return [fine, ring, scroll, purse, money]


def getOutlanderBackpack() -> List[I.Item]:
    staff = T.Tool("staff", "arcane focus", 5, "gp", 4, 1)
    hunting = T.Tool("hunting trap", "generic", 5, "gp", 25, 1)
    trophy = I.chooseAnimalTrophy()
    pouch = T.Tool("pouch", "generic", 5, "sp", 1, 1)
    money = I.Item("money", "money", 10, "gp", 1)
    return [staff, hunting, trophy, pouch, money]


def getSageBackpack() -> List[I.Item]:
    ink = T.Tool("black ink (1 ounce bottle)", "generic", 10, "gp", 0, 1)
    quill = T.Tool("quill", "generic", 0, "gp", 0, 1)
    knife = T.Tool("small knife", "generic", 0, "gp", 0, 1)
    letter = T.Tool("a letter from a dead colleague posing a question you have not yet been able to answer", "generic", 0, "gp", 0, 1)
    common = T.Tool("clothes, common", "generic", 5, "sp", 3, 1)
    pouch = T.Tool("pouch", "generic", 5, "sp", 1, 1)
    money = I.Item("money", "money", 10, "gp", 1)
    return [ink, quill, knife, letter, common, pouch, money]


def getSailorBackpack() -> List[I.Item]:
    club = W.Weapon("a belaying pin")
    rope = T.Tool("rope, silk (50 feet)", "generic", 10, "gp", 5, 1)
    trinket = I.chooseTrinket()
    common = T.Tool("clothes, common", "generic", 5, "sp", 3, 1)
    pouch = T.Tool("pouch", "generic", 5, "sp", 1, 1)
    money = I.Item("money", "money", 10, "gp", 1)
    return [club, rope, trinket, common, pouch, money]


def getSoldierBackpack() -> List[I.Item]:
    rank = I.Item("An insignia of rank", "generic", 0, "gp", 1)
    trophy = I.chooseFallenEnemyTrophy()
    game = T.chooseGamingSet(True)
    common = T.Tool("clothes, common", "generic", 5, "sp", 3, 1)
    pouch = T.Tool("pouch", "generic", 5, "sp", 1, 1)
    money = I.Item("money", "money", 10, "gp", 1)
    return [rank, trophy, game, common, pouch, money]


def getUrchinBackpack() -> List[I.Item]:
    knife = T.Tool("small knife", "generic", 0, "gp", 0, 1)
    map = T.Tool("a map of the city you grew up in", "generic", 1, "gp", 1, 1)
    # need to add beast
    mouse = I.Item("mouse", "rat", 0, "gp", 1)
    common = T.Tool("clothes, common", "generic", 5, "sp", 3, 1)
    pouch = T.Tool("pouch", "generic", 5, "sp", 1, 1)
    money = I.Item("money", "money", 10, "gp", 1)
    trinket = I.chooseTrinket()
    return [knife, map, mouse, common, pouch, money, trinket]

