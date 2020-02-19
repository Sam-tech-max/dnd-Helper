from typing import List
import Equipment.Tool as T


def getToolPro(background: str) -> List[str]:
    background = background.lower()
    if(background == "acolyte"):
        return getAcolyteToolPro()
    elif(background == "charlatan"):
        return getCharlatanToolPro()
    elif(background == "criminal"):
        return getCriminalToolPro()
    elif(background == "entertainer"):
        return getEntertainerToolPro()
    elif(background == "folk hero"):
        return getFolkHeroToolPro()
    elif(background == "guild artisan"):
        return getGuildArtisanToolPro()
    elif(background == "hermit"):
        return getHermitToolPro()
    elif(background == "noble"):
        return getNobleToolPro()
    elif(background == "outlander"):
        return getOutlanderToolPro()
    elif(background == "sage"):
        return getSageToolPro()
    elif(background == "sailor"):
        return getSailorToolPro()
    elif(background == "soldier"):
        return getSoldierToolPro()
    elif(background == "urchin"):
        return getUrchinToolPro()
    else:
        return getAcolyteToolPro()


def getAcolyteToolPro() -> List[str]:
    return []


def getCharlatanToolPro() -> List[str]:
    disguise = "disguise kit"
    forgery = "forgery kit"
    return [disguise, forgery]


def getCriminalToolPro() -> List[str]:
    gaming = (T.chooseGamingSet(False)).getName()
    thieves = "thieves' tools"
    return [gaming, thieves]

def getEntertainerToolPro() -> List[str]:
    disguise = "disguise kit"
    instrument = (T.chooseMusicalInstruments()).getName()
    return [disguise, instrument]


def getFolkHeroToolPro() -> List[str]:
    artisan = (T.chooseArtisanTool()).getName()
    vehicles = "vehicles (land)"
    return [artisan, vehicles]


def getGuildArtisanToolPro() -> List[str]:
    artisan = (T.chooseArtisanTool()).getName()
    return [artisan]


def getHermitToolPro() -> List[str]:
    herbalism = "herbalism kit"
    return [herbalism]


def getNobleToolPro() -> List[str]:
    gaming = (T.chooseGamingSet(False)).getName()
    return [gaming]


def getOutlanderToolPro() -> List[str]:
    instrument = (T.chooseMusicalInstruments()).getName()
    return [instrument]


def getSageToolPro() -> List[str]:
    return []


def getSailorToolPro() -> List[str]:
    navigator = "navigator's tools"
    vehicles = "vehicles (water)"
    return [navigator, vehicles]


def getSoldierToolPro() -> List[str]:
    gaming = (T.chooseGamingSet(False)).getName()
    vehicles = "vehicles (land)"
    return [gaming, vehicles]


def getUrchinToolPro() -> List[str]:
    disguise = "disguise kit"
    thieves = "thieves' tools"
    return [disguise, thieves]

