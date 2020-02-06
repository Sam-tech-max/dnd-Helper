import Races.Race as r
import Stats as s
from typing import List


class Halfling(r.Race):
    def __init__(self, age: int=20, alignment: str="lawful good",
                 height: int=36, stats: s.Stats=s.Stats(),
                 subrace: str="lightfoot", weight: int=40,
                 gender: str="male", firstName: str="alton",
                 lastName: str="brushgather"):
        subrace = subrace.lower()
        self.featuresAndTraits = ["lucky: When you roll a 1 on an attack roll, ability check, or saving throw, you can reroll the die and must use the new roll",
                                  "brave: You have advantage on saving throws against being frightened",
                                  "halfling nimblesness: you can move through the space of any creature that is of a size larger than yours."]
        if(subrace == "lightfoot"):
            self.featuresAndTraits.append("naturally stealthy: You can attempt to hide even when you are obscured only by a creature that is at least one size larger than you.")
        elif(subrace == "stout"):
            self.featuresAndTraits.append("stout resilience: You have advantage on saving throws against poison, and you have resistance against poison damage.")
        else:
            self.featuresAndTraits.append("naturally stealthy: You can attempt to hide even when you are obscured only by a creature that is at least one size larger than you.")

        super().__init__("halfling", age, alignment, height,
                         "common halfling", "small", stats, 25,
                         subrace, weight, gender, firstName,
                         lastName)


#//----------// //----------// //----------//
# Other methods associatied with the Elf race
#//----------// //----------// //----------//
    def abilityScoreIncrease(self):
        stats = self.getStats()
        print("Your Dexterity score increases by 2.")
        dex = stats.getStat("dexterity")
        dex.setScore(dex.getScore() + 2)
        stats.setStat(dex)
        if(super().getSubrace() == "lightfoot"):
            print("Your Charisma score increases by 1")
            cha = stats.getStat("charisma")
            cha.setScore(cha.getScore() + 1)
            stats.setStat(cha)
        elif(super().getSubrace() == "stout"):
            print("Your Consitiution score increases by 1.")
            con = stats.getStat("constitution")
            con.setScore(con.getScore() + 1)
            stats.setStat(con)
        super().setStats(stats)

#//----------// //----------// //----------//
# Print methods:
# These methods will print out all of the
# variables.
#//----------// //----------// //----------//
    def printRace(self, printStats: bool):
        super().printRace(printStats)
        self.printFeaturesAndTraits()
    
    def printFeaturesAndTraits(self):
        print("//----------// features and traits //----------//")
        for fat in self.getFeaturesAndTraits():
            print(fat)
        print("//----------// //----------// //----------//")


#//----------// //----------// //----------//
# Check methods:
# These methods will give a boolean value.
#//----------// //----------// //----------//
    def checkAge(self, age: int) -> int:
        if(age < 0):
            print("You are too young. Setting age to 100.")
            return 20
        elif(age > 250):
            print("You are too old. Setting age to 250.")
            return 250
        else:
            return age

    # checks that the halfling is at least medium hight
    # which is 24 in to 48 in
    def checkHeight(self, height: int) -> bool:
        if(height >= 24 and height <= 48):
            return True
        else:
            return False

    def checkSubrace(self, subrace: str) -> bool:
        subrace = subrace
        if(subrace == "lightfoot" or subrace == "stout"):
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

    def getFeaturesAndTraits(self) -> List[str]:
        return self.featuresAndTraits

    def setFeaturesAndTraits(self, featuresAndTraits: List[str]):
        self.featuresAndTraits = featuresAndTraits

    def getHeight(self) -> int:
        if(not self.checkHeight(self.height)):
            self.setHeight(60)
        return self.height

    def setHeight(self, height: int):
        if(self.checkHeight(height)):
            super().setHeight(height)
        else:
            print("Height not a small creature. A halfling is a small creature between 2 ft and 4 ft")
            super().setHeight(24)

    def getSubrace(self) -> str:
        if(self.checkSubrace(self.subrace)):
            return self.subrace
        else:
            self.setSubrace("lightfoot")
            return self.subrace

    def setSubrace(self, subrace: str):
        if(not self.checkSubrace(subrace)):
            subrace = "lightfoot"
        self.subrace = subrace

#//----------// //----------// //----------//
# Main Class
#//----------// //----------// //----------//





