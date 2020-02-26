import Races.Stats as S
import Equipment.Item as I
import Equipment.Weapon as W
from typing import List


def checkDie(die: int = 0) -> bool:
    if(die == 4 or die == 6 or die == 8 or die == 10 or die == 12 or
       die == 20 or die == 100):
        return True
    return False


def genericChoose(skill: str, options: List[str]):
    print("Please choose a", skill, ":")
    enter = 0
    while(len(options) > enter):
        print("Enter", enter, "for", options[enter])
        enter += 1
    op = int(input())
    if(op < 0):
        return genericChoose(skill, options)
    elif(op > len(options)):
        return genericChoose(skill, options)
    else:
        return options[op]


def getProficiencyByLevel(level: int = 1) -> int:
    if(level < 5):
        return 2
    elif(level < 9):
        return 3
    elif(level < 13):
        return 4
    elif(level < 17):
        return 5
    else:
        return 6


def maxMinIntCheck(max:int = 0, min: int = 1, num: int = 0) -> int:
    if(num < min):
        return min
    elif(num > max):
        return max
    else:
        return num


class PlayerClass(object):
    
    def __init__(self,
                 charisma: int = 3,
                 className: str = "",
                 constitution: int = 3,
                 dexterity: int = 3,
                 health: int = 1,
                 hitDie: int = 8,
                 intelligence: int = 3,
                 level: int = 1,
                 otherItems: List[I.Item] = [],
                 proficiencies: List[str] = [],
                 savingThrows: List[str] = [],
                 skills: List[str] = [],
                 strength: int = 3,
                 weapons: List[W.Weapon] = [],
                 wisdom: int = 3):
        charisma = maxMinIntCheck(18, 3, charisma)
        self.className = className
        constitution = maxMinIntCheck(18, 3, constitution)
        dexterity = maxMinIntCheck(18, 3, dexterity)
        self.health = int(maxMinIntCheck(1000000, 3, health))
        if(checkDie(hitDie)):
            self.hitDie = hitDie
        else:
            self.hitDie = 8
        intelligence = maxMinIntCheck(18, 3, intelligence)
        self.level = maxMinIntCheck(20, 1, level)
        self.otherItems = otherItems
        self.proficiencies = proficiencies
        self.proficiencyBonus = getProficiencyByLevel(self.level)
        self.savingThrows = savingThrows
        self.skills = skills
        strength = maxMinIntCheck(18, 3, strength)
        self.weapons = weapons
        wisdom = maxMinIntCheck(18, 3, wisdom)
        self.stats = S.Stats(self.proficiencyBonus, strength,
                             dexterity, constitution, intelligence,
                             wisdom, charisma)
        self.stats.calculateMods()

# //---------// //---------// //---------//
# These are the print methods
# //---------// //---------// //---------//
    def printPlayerClass(self, printStats: bool = False):
        print("Class:", self.getClassName())
        print("Hit Die:", self.getHitDie())
        print("Level", self.getLevel())
        self.printProficiencies()
        print("proficiencyBonus:", self.getProficiencyBonus())
        print("health:", self.getHealth())
        self.printSavingThrows()
        self.printSkills()
        if(printStats):
            self.stats.printStats()
        self.printWeapons()
        self.printOtherItems()


    def printOtherItems(self):
        print("//----------// Other Items //----------//")
        for item in self.getOtherItems():
            item.printItem()
        print("//----------// //----------// //----------//")


    def printProficiencies(self):
        d = ""
        for p in self.getProficiencies():
            d += ":" + p + ":"
        print(d)


    def printSavingThrows(self):
        d = ""
        for st in self.getSavingThrows():
            d += ":" + st + ":"
        print(d)


    def printSkills(self):
        d = ""
        for sk in self.getSkills():
            d += ":" + sk + ":"
        print(d)


    def printWeapons(self):
        print("//----------// Weapons //----------//")
        for weapon in self.getWeapons():
            weapon.printItem()
        print("//----------// //----------// //----------//")


    def levelUp(self):
        if(self.getLevel() >= 20):
            self.setLevel(20)
        else:
            self.setLevel(self.getLevel() + 1)


# //---------// //---------// //---------//
# These are the get and set methods
# //---------// //---------// //---------//
    def getClassName(self) -> str:
        return self.className

    def setClassName(self, className: str = "") -> str:
        self.className = className
        return self.className

    def getHealth(self) -> int:
        return self.health

    def setHealth(self, health):
        if(health < 1):
            self.health = 1
        else:
            self.health = health

    def getHitDie(self) -> int:
        return self.hitDie

    def setHitDie(self, hitDie: int = 8) -> int:
        if(checkDie(hitDie)):
            self.hitDie = hitDie
        else:
            self.hitDie = 8
        return self.hitDie

    def getLevel(self) -> int:
        return self.level

    def setLevel(self, level: int = 1) -> int:
        if(level < 1):
            self.level = 1
        elif(level > 20):
            self.level = 20
        else:
            self.level = level
        return self.level

    def getOtherItems(self) -> List[I.Item]:
        return self.otherItems

    def setOtherItems(self, items: List[I.Item] = []) -> List[I.Item]:
        self.otherItems = items
        return self.otherItems

    def getProficiencies(self) -> List[str]:
        return self.proficiencies

    def setProficiencies(self, proficiencies: List[str]) -> List[str]:
        self.proficiencies = proficiencies
        return self.proficiencies

    def getProficiencyBonus(self) -> int:
        return self.proficiencyBonus

    def setProficiencyBonus(self, proficiencyBonus: int = 2) -> int:
        self.proficiencyBonus = proficiencyBonus
        return self.proficiencyBonus

    def getSavingThrows(self) -> List[str]:
        return self.savingThrows

    def setSavingThrows(self, savingThrows: List[str] = []) -> List[str]:
        self.savingThrows = savingThrows
        return self.savingThrows

    def getSkills(self) -> List[str]:
        return self.skills

    def setSkills(self, skills: List[str]) -> List[str]:
        self.skills = skills
        return self.skills

    def getWeapons(self) -> List[W.Weapon]:
        return self.weapons

    def setWeapons(self, weapons: List[W.Weapon]) -> List[W.Weapon]:
        self.weapons = weapons
        return self.weapons


# //---------// //---------// //---------//
# Main Statements
# //---------// //---------// //---------//
