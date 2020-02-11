import Equipment.Item as I
from typing import List


def getEquipment(background: str) -> List[I.Item]:
    background = background.lower()
    if(background == "acolyte"):
        return getAcolyteEquipment()
    elif(background == "charlatan"):
        return getCharlatanEquipment()
    elif(background == "criminal"):
        return getCriminalEquipment()
    elif(background == "entertainer"):
        return getEntertainerEquipment()
    elif(background == "folk hero"):
        return getFolkHeroEquipment()
    elif(background == "guild artisan"):
        return getGuildArtisanEquipment()
    elif(background == "noble"):
        return getNobleEquipment()
    elif(background == "outlander"):
        return getOutlanderEquipment()
    elif(background == "sage"):
        return getSageEquipment()
    elif(background == "sailor"):
        return getSailorEquipment()
    elif(background == "soldier"):
        return getSoldierEquipment()
    elif(background == "urchin"):
        return getUrchinEquipment()
    else:
        return getAcolyteEquipment()


def getAcolyteEquipment() -> List[I.Item]:
    return [I.Item()]


def getCharlatanEquipment() -> List[I.Item]:
    return [I.Item()]


def getCriminalEquipment() -> List[I.Item]:
    return [I.Item()]


def getEntertainerEquipment() -> List[I.Item]:
    return [I.Item()]


def getFolkHeroEquipment() -> List[I.Item]:
    return [I.Item()]


def getGuildArtisanEquipment() -> List[I.Item]:
    return [I.Item()]


def getHermitEquipment() -> List[I.Item]:
    return [I.Item()]


def getNoble() -> List[I.Item]:
    return [I.Item()]


def getOutlanderEquipment() -> List[I.Item]:
    return [I.Item()]


def getSageEquipment() -> List[I.Item]:
    return [I.Item()]


def getSailorEquipment() -> List[I.Item]:
    return [I.Item()]


def getSoldierEquipment() -> List[I.Item]:
    return [I.Item()]


def getUrchin() -> List[I.Item]:
    return [I.Item()]

