import Race as r
import Stats as s
from typing import List

class HalfOrc(r.Race):
    def __init__(self, age: int=14, alignment: str="chaotic evil",
                 height: int=60, stats: s.Stats=s.Stats(),
                 weight: int=200, gender: str="male",
                 firstName: str="dench", lastName: str="basha"):
        intimidation = stats.getStat("charisma: intimidation")
        intimidation.setHasProficiency(True)
        stats.setStat(intimidation)
        super().__init__("half-orc", age, alignment, height,
                         "common orc", "medium", stats, 30, "none",
                         weight, gender, firstName, lastName)
        self.darkvision = 60
        self.featuresAndTraits = ["relentless endurance: When you are reduced to 0 hit points but not killed outright, you can drop to 1 hit point instead. You can’t use this feature again until you finish a long rest",
                                  "savage attacks: When you score a critical hit with a melee weapon attack, you can roll one of the weapon’s damage dice one additional time and add it to the extra damage of the critical hit"]


#//----------// //----------// //----------//
# Other methods associatied with the Human race
#//----------// //----------// //----------//
    def abilityScoreIncrease(self):
        stats = self.getStats()

        print("Your Strength score increases by 2")
        strength = stats.getStat("strength")
        strength.setScore(strength.getScore() + 2)
        stats.setStat(strength)

        print("Your Constitution score increases by 1")
        con = stats.getStat("constitution")
        con.setScore(con.getScore() + 1)
        stats.setStat(con)

        super().setStats(stats)

#//----------// //----------// //----------//
# Print methods:
# These methods will print out all of the
# variables.
#//----------// //----------// //----------//
    def printRace(self, showStats: bool):
        super().printRace(showStats)
        print("Darkvision:", self.getDarkvision(), "ft")
        self.printFeaturesAndTraits()

    def printFeaturesAndTraits(self):
        print("//----------// Features and Traits //----------//")
        for each in self.getFeaturesAndTraits():
            print(each)
        print("//----------// //----------// //----------//")


#//----------// //----------// //----------//
# Check methods:
# These methods will give a boolean value.
#//----------// //----------// //----------//
    def checkAge(self, age: int) -> int:
        if(age < 0):
            print("You are too young. Setting age to 14.")
            return 14
        elif(age > 75):
            print("You are too old. Setting age to 75.")
            return 75
        else:
            return age

    # checks that the orc is at least medium hight
    # which is 48 in to 96 ft
    def checkHeight(self, height: int) -> bool:
        if(height >= 48 and height <= 96):
            return True
        else:
            return False

    def checkSubrace(self, subrace: str) -> bool:
        subrace = subrace
        if(subrace == "none"):
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
        self.darkvision = darkvision

    def getHeight(self) -> int:
        if(not self.checkHeight(self.height)):
            self.setHeight(60)
        return self.height

    def setHeight(self, height: int):
        if(self.checkHeight(height)):
            super().setHeight(height)
        else:
            print("Height not a medium creature. A half-orc is a medium creature between 5 ft and 6 ft, but medium creatures are between 4 ft and 8 ft")
            super().setHeight(60)

    def getFeaturesAndTraits(self) -> List[str]:
        return self.featuresAndTraits

    def setFeaturesAndTraits(self, featuresAndTraits: List[str]):
        self.featuresAndTraits = featuresAndTraits

    def getSubrace(self) -> str:
        if(self.checkSubrace(self.subrace)):
            return self.subrace
        else:
            self.setSubrace("none")
            return self.subrace

    def setSubrace(self, subrace: str):
        if(not self.checkSubrace(subrace)):
            subrace = "none"
        self.subrace = subrace

#//----------// //----------// //----------//
# Main Class
#//----------// //----------// //----------//
h = HalfOrc()
h.printRace(False)
h.abilityScoreIncrease()
h.printRace(False)







