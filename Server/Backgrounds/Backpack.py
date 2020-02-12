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
    return [fineClothes, disguiseKit, conTool]


def getCriminalBackpack() -> List[I.Item]:
    return [I.Item()]


def getEntertainerBackpack() -> List[I.Item]:
    return [I.Item()]


def getFolkHeroBackpack() -> List[I.Item]:
    return [I.Item()]


def getGuildArtisanBackpack() -> List[I.Item]:
    return [I.Item()]


def getHermitBackpack() -> List[I.Item]:
    return [I.Item()]


def getNobleBackpack() -> List[I.Item]:
    return [I.Item()]


def getOutlanderBackpack() -> List[I.Item]:
    return [I.Item()]


def getSageBackpack() -> List[I.Item]:
    return [I.Item()]


def getSailorBackpack() -> List[I.Item]:
    return [I.Item()]


def getSoldierBackpack() -> List[I.Item]:
    return [I.Item()]


def getUrchinBackpack() -> List[I.Item]:
    return [I.Item()]

