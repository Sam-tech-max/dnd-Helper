import Classes.PlayerClass as PC
from typing import List
import Races.Stats as S
import Equipment.Weapon as W

def maxMinIntCheck(max:int = 0, min: int = 1, num: int = 0) -> int:
    if(num < min):
        return min
    elif(num > max):
        return max
    else:
        return num

def getRageByLevel(level:int = 1) -> int:
    if(level < 3):
        return 2
    elif(level < 6):
        return 3
    elif(level < 12):
        return 4
    elif(level < 17):
        return 5
    elif(level < 20):
        return 6
    else:
        return 1000000

class Barbarian(PC.PlayerClass):
    def __init__(self,
                 charisma: int = 3,
                 constitution: int = 3,
                 dexterity: int = 3,
                 health: int = 1,
                 intelligence: int = 3,
                 level: int = 1,
                 skillsAlready: List[str] = [],
                 chooseSkill: List[str] = [],
                 strength: int = 3,
                 wisdom: int = 3):
        # conMod at first level
        if(health < 8):
            health = int((((maxMinIntCheck(18, 3, constitution) -
                            (maxMinIntCheck(18, 3, constitution) %
                             2)) - 10)/2) + 12)
        
        skills = ["wisdom: animal handling", "strength: athletics",
                  "charisma: intimidation", "intelligence: nature",
                  "wisdom: perception", "wisdom: survival"]
        
        for skill in skillsAlready:
            skills.remove(skill)
        skill1 = PC.genericChoose("skill", skills)
        skills.remove(skill1)
        skill2 = PC.genericChoose("skill", skills)
        weapon1 = PC.genericChoose("weapon", ["battleaxe", "flail",
                                              "glaive", "greataxe",
                                              "greatsword",
                                              "halberd", "lance",
                                              "longsword", "maul",
                                              "morningstar", "pike",
                                              "rapier", "scimitar",
                                              "shortsword",
                                              "trident", "war pick",
                                              "warhammer", "whip"])
        weapon2 = PC.genericChoose("weapon", ["club", "dagger", "greatclub", "2 handaxe", "javelin", "light hammer", "mace", "quarterstaff", "sickle", "spear"])
        if("2" in weapon2):
            weapon2 = W.getSimpleMeleeByName("handaxe", 2)
        else:
            weapon2 = W.getSimpleMeleeByName(weapon2)
        super().__init__(charisma,
                         "barbarian",
                         constitution,
                         dexterity,
                         health,
                         12,
                         intelligence,
                         level,
                         [],
                         ["light armor", "medium armor", "shields", "simple weapons", "martial weapons"],
                         ["strength", "constitution"],
                         [skill1, skill2],
                         strength,
                         [W.getMartialMeleeByName(weapon1), weapon2, W.getSimpleMeleeByName("javelin", 5)],
                         wisdom)
        self.rage = getRageByLevel(self.getLevel())


    def printPlayerClass(self):
        super().printPlayerClass()
        print("Rage:", self.getRage())
        print("Rage Damage: +", self.getRageDamage())


    def levelUp(self, d12Roll: int = 1):
        super().levelUp()
        conStat = self.stats.getStat("constitution")
        self.setHealth(self.getHealth() + d12Roll + conStat.getMod())


# //---------// //---------// //---------//
# These are the get and set methods
# //---------// //---------// //---------//
    def getRage(self) -> int:
        return self.rage

    def setRage(self, rage: int) -> int:
        if(rage < 2):
            rage = 2
        elif(rage < 7 or rage == getRageByLevel(20)):
            self.rage = rage
        else:
            self.rage = getRageByLevel(self.getLevel())
        return self.rage


    def getRageDamage(self) -> int:
        if(self.getLevel() < 9):
            return 2
        elif(self.getLevel() < 16):
            return 3
        else:
            return 4


# //---------// //---------// //---------//
# Main Statements
# //---------// //---------// //---------//
barb = Barbarian(8, 12, 15, 0, 10, 1,
                 ["wisdom: animal handling", "strength: athletics"],
                 [], 17, 16)
barb.printPlayerClass()
barb.levelUp(11)
barb.printPlayerClass()
