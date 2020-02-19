import Classes.PlayerClass as PC
import Races.Stats as S

def maxMinIntCheck(max:int = 0, min: int = 1, num: int = 0) -> int:
    if(num < min):
        return min
    elif(num > max):
        return max
    else:
        return num

class Barbarian(PC.PlayerClass):
    def __init__(self,
                 charisma: int = 3,
                 constitution: int = 3,
                 dexterity: int = 3,
                 health: int = 1,
                 intelligence: int = 3,
                 level: int = 1,
                 strength: int = 3,
                 wisdom: int = 3):
        # conMod at first level
        if(health < 8):
            health = int((((maxMinIntCheck(18, 3, constitution) - (maxMinIntCheck(18, 3, constitution) % 2)) - 10)/2) + 12)
        super().__init__(charisma, "barbarian", constitution,
                         dexterity, health, intelligence, 12, level,
                         strength, wisdom)




# //---------// //---------// //---------//
# Main Statements
# //---------// //---------// //---------//
barb = Barbarian(8, 12, 15, 0, 10, 1, 17, 16)
barb.printPlayerClass()
