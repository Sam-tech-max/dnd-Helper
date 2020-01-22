import Race as r
import Stats as s

class Dwarf(r.Race):
    def __init__(self, age: int=50, alignment: str="lawful good",
                 height: int=48, stats: s.Stats=s.Stats(),
                 subrace: str="hill", weight: int=150):
        super().__init__("dwarf", age, alignment, height,
                         "common dwarvish", "medium", stats, 25,
                         subrace, weight)
        self.darkvision = 60

#//----------// //----------// //----------//
# Other methods associatied with the Dwarf race
#//----------// //----------// //----------//
    def abilityScoreIncrease(self):
        stats = self.getStats()
        print("Your Constitution score increases by 2.")
        con = stats.getStat("constitution")
        con.setScore(con.getScore() + 2)
        stats.setStat(con)
        if(super().getSubrace() == "hill"):
            print("Your Wisdom score increases by 1.")
        elif(super().getSubrace() == "mountain"):
            print("Your Strength score increases by 2")
        super().setStats(stats)

#//----------// //----------// //----------//
# Print methods:
# These methods will print out all of the
# variables.
#//----------// //----------// //----------//
    def printDwarf(self):
        super().printRace()
        print("Darkvision:", self.getDarkvision())

#//----------// //----------// //----------//
# Check methods:
# These methods will give a boolean value.
#//----------// //----------// //----------//
    def checkAge(self, age: int) -> int:
        if(age < 0):
            print("You are too young. Setting age to 50.")
            return 50
        elif(age > 350):
            print("You are too old. Setting age to 350.")
            return 350
        else:
            return age

    # checks that the dwarf is at least medium hight
    # which is 48 in to 96 ft
    def checkHeight(self, height: int) -> bool:
        if(height >= 48 and height <= 96):
            return True
        else:
            return False

    def checkSubrace(self, subrace: str) -> bool:
        subrace = subrace
        if(subrace == "hill" or subrace == "mountain"):
            return True
        else:
            return False


#//----------// //----------// //----------//
# Get and Set methods
#//----------// //----------// //----------//
    def getAge(self) -> int:
        age = self.checkAge(self.age)
        if(age == self.age):
            return age
        else:
            self.setAge(age)
            return age

    def setAge(self, age: int):
        age = self.checkAge(age)
        self.age = age

    def getDarkvision(self) -> int:
        return self.darkvision

    def setDarkvision(self, darkvision:int):
        if(darkvision > 60):
            self.darkvision = darkvision

    def getHeight(self) -> int:
        if(not self.checkHeight(48)):
            self.setHeight(48)
        return self.height

    def setHeight(self, height: int):
        if(self.checkHeight(height)):
            super().setHeight(height)
        else:
            print("Height not a medium creature. A dwarf is a medium creature between 4 ft and 5 ft, but medium creatures are between 4 ft and 8 ft")
            super().setHeight(48)

    def getSubrace(self) -> str:
        if(self.checkSubrace(self.subrace)):
            return self.subrace
        else:
            self.setSubrace("hill")
            return self.subrace

    def setSubrace(self, subrace: str):
        if(self.checkSubrace(subrace)):
            subrace = "hill"
        self.subrace = subrace

#//----------// //----------// //----------//
# Main Class
#//----------// //----------// //----------//
d = Dwarf()
d.printDwarf()
d.abilityScoreIncrease()