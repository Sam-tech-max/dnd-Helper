from typing import List


def getSkillPro(background: str) -> List[str]:
    background = background.lower()
    if(background == "acolyte"):
        return getAcolyteSkillPro()
    elif(background == "charlatan"):
        return getCharlatanSkillPro()
    elif(background == "criminal"):
        return getCriminalSkillPro()
    elif(background == "entertainer"):
        return getEntertainerSkillPro()
    elif(background == "folk hero"):
        return getFolkHeroSkillPro()
    elif(background == "guild artisan"):
        return getGuildArtisanSkillPro()
    elif(background == "hermit"):
        return getHermitSkillPro()
    elif(background == "noble"):
        return getNobleSkillPro()
    elif(background == "outlander"):
        return getOutlanderSkillPro()
    elif(background == "sage"):
        return getSageSkillPro()
    elif(background == "sailor"):
        return getSailorSkillPro()
    elif(background == "soldier"):
        return getSoldierSkillPro()
    elif(background == "urchin"):
        return getUrchinSkillPro()
    else:
        return getAcolyteSkillPro()


def getAcolyteSkillPro() -> List[str]:
    insight = "wisdom: insight"
    religion = "intelligence: religion"
    return [insight, religion]


def getCharlatanSkillPro() -> List[str]:
    deception = "charisma: deception"
    sleight = "dexterity: sleight of hand"
    return [deception, sleight]


def getCriminalSkillPro() -> List[str]:
    deception = "charisma: deception"
    stealth = "dexterity: stealth"
    return [deception, stealth]

def getEntertainerSkillPro() -> List[str]:
    acrobatics = "dexterity: acrobatics"
    performace = "charisma: performance"
    return [acrobatics, performace]


def getFolkHeroSkillPro() -> List[str]:
    animal = "wisdom: animal handling"
    survival = "wisdom: survival"
    return [animal, survival]


def getGuildArtisanSkillPro() -> List[str]:
    insight = "wisdom: insight"
    persuasion = "charisma: persuasion"
    return [insight, persuasion]


def getHermitSkillPro() -> List[str]:
    medicine = "wisdom: medicine"
    religion = "intelligence: religion"
    return [medicine, religion]


def getNobleSkillPro() -> List[str]:
    history = "intelligence: history"
    persuasion = "charisma: persuasion"
    return [history, persuasion]


def getOutlanderSkillPro() -> List[str]:
    athletics = "strength: atheletics"
    survival = "wisdom: survival"
    return [athletics, survival]


def getSageSkillPro() -> List[str]:
    arcana = "intelligence: arcana"
    history = "intelligence: history"
    return [arcana, history]


def getSailorSkillPro() -> List[str]:
    athletics = "strength: atheletics"
    perception = "wisdom: perception"
    return [athletics, perception]


def getSoldierSkillPro() -> List[str]:
    athletics = "strength: atheletics"
    intimidation = "charisma: intimidation"
    return [athletics, intimidation]


def getUrchinSkillPro() -> List[str]:
    sleight = "dexterity: sleight of hand"
    stealth = "dexterity: stealth"
    return [sleight, stealth]

