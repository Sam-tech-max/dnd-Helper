import Races.Stats as S

def checkDie(die: int = 0) -> bool:
    if(die == 4 or die == 6 or die == 8 or die == 10 or die == 12 or
       die == 20 or die == 100):
        return True
    return False


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
                 strength: int = 3,
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
        self.proficiencyBonus = getProficiencyByLevel(self.level)
        strength = maxMinIntCheck(18, 3, strength)
        wisdom = maxMinIntCheck(18, 3, wisdom)
        self.stats = S.Stats(self.proficiencyBonus, strength,
                             dexterity, constitution, intelligence,
                             wisdom, charisma)


    def printPlayerClass(self):
        print("Class:", self.getClassName())
        print("Hit Die:", self.getHitDie())
        print("Level", self.getLevel())
        print("proficiencyBonus:", self.getProficiencyBonus())
        print("health:", self.getHealth())

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

    def getProficiencyBonus(self) -> int:
        return self.proficiencyBonus

    def setProficiencyBonus(self, proficiencyBonus: int = 2) -> int:
        self.proficiencyBonus = proficiencyBonus
        return self.proficiencyBonus


# //---------// //---------// //---------//
# Main Statements
# //---------// //---------// //---------//
