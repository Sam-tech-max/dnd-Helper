import Equipment.Item as I
import Equipment.Tool as T
from typing import List


def getPackByName(name: str = "burglar") -> List[I.Item]:
    if(name == "burglar"):
        return getBurglarPack()
    elif(name == "diplomat"):
        return getDiplomatPack()
    elif(name == "dungeoneer"):
        return getDungeoneerPack()
    elif(name == "entertainer"):
        return getEntertainerPack()
    elif(name == "explorer"):
        return getExplorerPack()
    elif(name == "priest"):
        return getPriestPack()
    elif(name == "scholar"):
        return getScholarPack()
    else:
        return []


def getBurglarPack() -> List[I.Item]:
    backpack = T.getToolByName("backpack")
    bearings = T.getToolByName("ball bearings (bag of 1000)")
    string = I.Item("string (10-feet)", "generic", 0, "gp", 1)
    bell = T.getToolByName("bell")
    candles = T.getToolByName("candle", 5)
    crowbar = T.getToolByName("crowbar")
    hammer = T.getToolByName("hammer")
    pitons = T.getToolByName("piton", 10)
    lantern = T.getToolByName("hooded lantern")
    oil = T.getToolByName("oil (flask)", 2)
    rations = T.getToolByName("ration", 5)
    tinderbox = T.getToolByName("tinderbox")
    waterskin = T.getToolByName("waterskin")
    rope = T.getToolByName("hempen rope (50 feet)")

    pack = [backpack, bearings, string, bell, candles, crowbar,
            hammer, pitons, lantern, oil,rations, tinderbox,
            waterskin, rope]
    pack.sort()

    return pack


def getDiplomatPack() -> List[I.Item]:
    chest = T.getToolByName("chest")
    map = T.getToolByName("map case")
    scroll = T.getToolByName("scroll case")
    fine = T.getToolByName("fine clothes")
    ink = T.getToolByName("ink (1 ounce bottle)")
    pen = T.getToolByName("ink pen")
    lamp = T.getToolByName("lamp")
    oil = T.getToolByName("oil (flask)", 2)
    paper = T.getToolByName("paper", 5)
    perfume = T.getToolByName("perfume (vial)")
    wax = T.getToolByName("sealing wax")
    soap = T.getToolByName("soap")

    pack = [chest, map, scroll, fine, ink, pen, lamp, oil, paper,
            perfume, wax, soap]
    pack.sort()

    return pack


def getDungeoneerPack() -> List[I.Item]:
    backpack = T.getToolByName("backpack")
    crowbar = T.getToolByName("crowbar")
    hammer = T.getToolByName("hammer")
    pitons = T.getToolByName("piton", 10)
    torch = T.getToolByName("torch", 10)
    tinderbox = T.getToolByName("tinderbox")
    rations = T.getToolByName("ration", 10)
    waterskin = T.getToolByName("waterskin")
    rope = T.getToolByName("hempen rope (50 feet)")

    pack = [backpack, crowbar, hammer, pitons, torch, tinderbox,
            rations, waterskin, rope]
    pack.sort()

    return pack


def getEntertainerPack() -> List[I.Item]:
    backpack = T.getToolByName("backpack")
    bedroll = T.getToolByName("bedroll")
    costume = T.getToolByName("costume clothes", 2)
    candle = T.getToolByName("candle", 5)
    ration = T.getToolByName("ration", 5)
    waterskin = T.getToolByName("waterskin")
    disguise = T.getToolByName("disguise kit")

    pack = [backpack, bedroll, costume, candle, ration, waterskin,
            disguise]
    pack.sort()

    return pack


def getExplorerPack() -> List[I.Item]:
    backpack = T.getToolByName("backpack")
    bedroll = T.getToolByName("bedroll")
    mess = T.getToolByName("mess kit")
    tinderbox = T.getToolByName("tinderbox")
    torches = T.getToolByName("torch", 10)
    rations = T.getToolByName("ration", 10)
    water = T.getToolByName("waterskin")
    rope = T.getToolByName("hempen rope (50 feet)")
    
    pack = [backpack, bedroll, mess, tinderbox, torches, rations,
            water, rope]
    pack.sort()

    return pack


def getPriestPack() -> List[I.Item]:
    backpack = T.getToolByName("backpack")
    blanket = T.getToolByName("blanket")
    candles = T.getToolByName("candle", 10)
    tinderbox = T.getToolByName("tinderbox")
    alms = I.Item("alms box", "generic", 0, "gp", 1)
    incense = I.Item("block of incense", "generic", 0, "gp", 2)
    censer = I.Item("censer", "generic", 0, "gp", 1)
    vestments = I.Item("vestments", "generic", 0, "gp", 1)
    rations = T.getToolByName("ration", 2)
    water = T.getToolByName("waterskin")

    pack = [backpack, blanket, candles, tinderbox, alms, incense,
            censer, vestments, rations, water]
    pack.sort()
    return pack


def getScholarPack() -> List[I.Item]:
    backpack = T.getToolByName("backpack")
    book = T.getToolByName("book")
    book.setName("book of lore")
    ink = T.getToolByName("ink (1 ounce bottle)")
    pen = T.getToolByName("ink pen")
    parchment = T.getToolByName("parchment", 10)
    sand = I.Item("little bag of sand", "generic", 0, "gp", 1)
    knife = I.Item("small knife", "generic", 0, "gp", 1)

    pack = [backpack, book, ink, pen, parchment, sand, knife]
    pack.sort()

    return pack



