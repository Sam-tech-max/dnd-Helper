import Races.Race as r
import Stats as s
from typing import List

class HalfElf(r.Race):
    def __init__(self, age: int=20, alignment: str="chaotic good",
                 height: int=60, stats: s.Stats=s.Stats(),
                 weight: int=150, gender: str="male",
                 firstName: str="aseir", lastName: str="basha"):
        l = r.chooseLanguage()
        super().__init__("half-elf", age, alignment, height,
                         "common elvish" + l, "medium", stats, 30,
                         "none", weight, firstName, lastName)
        self.darkvision = 60
        self.featuresAndTraits = ["fey ancestry: You have advantage on saving throws against being charmed and magic can't put you to sleep."]

#//----------// //----------// //----------//
# Other methods associatied with the Human race
#//----------// //----------// //----------//
    def abilityScoreIncrease(self):
        stats = self.getStats()
        print("Your Charisma score increases by 2")
        cha = stats.getStat("charisma")
        cha.setScore(cha.getScore() + 2)
        stats.setStat(cha)
        s1 = r.chooseStat()
        if(s1 == "dexterity"):
            print("Your Dexterity score increases by 1.")
            dex = stats.getStat("dexterity")
            dex.setScore(dex.getScore() + 1)
            stats.setStat(dex)
        elif(s1 == "charisma"):
            print("Your Charisma score increases by 1")
            cha = stats.getStat("charisma")
            cha.setScore(cha.getScore() + 1)
            stats.setStat(cha)
        elif(s1 == "intelligence"):
            print("Your Intelligence score increases by 1.")
            intell = stats.getStat("intelligence")
            intell.setScore(intell.getScore() + 1)
            stats.setStat(intell)
        elif(s1 == "wisdom"):
            print("Your Wisdom score increases by 1")
            wis = stats.getStat("wisdom")
            wis.setScore(wis.getScore() + 1)
            stats.setStat(wis)
        elif(s1 == "strength"):
            print("Your Strength score increases by 1")
            strength = stats.getStat("strength")
            strength.setScore(strength.getScore() + 1)
            stats.setStat(strength)
        elif(s1 == "constitution"):
            print("Your Constitution score increases by 1")
            con = stats.getStat("constitution")
            con.setScore(con.getScore() + 1)
            stats.setStat(con)
        s2 = r.chooseStat()
        if(s2 == "dexterity"):
            print("Your Dexterity score increases by 1.")
            dex = stats.getStat("dexterity")
            dex.setScore(dex.getScore() + 1)
            stats.setStat(dex)
        elif(s2 == "charisma"):
            print("Your Charisma score increases by 1")
            cha = stats.getStat("charisma")
            cha.setScore(cha.getScore() + 1)
            stats.setStat(cha)
        elif(s2 == "intelligence"):
            print("Your Intelligence score increases by 1.")
            intell = stats.getStat("intelligence")
            intell.setScore(intell.getScore() + 1)
            stats.setStat(intell)
        elif(s2 == "wisdom"):
            print("Your Wisdom score increases by 1")
            wis = stats.getStat("wisdom")
            wis.setScore(wis.getScore() + 1)
            stats.setStat(wis)
        elif(s2 == "strength"):
            print("Your Strength score increases by 1")
            strength = stats.getStat("strength")
            strength.setScore(strength.getScore() + 1)
            stats.setStat(strength)
        elif(s2 == "constitution"):
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
            print("You are too young. Setting age to 20.")
            return 20
        elif(age > 180):
            print("You are too old. Setting age to 180.")
            return 180
        else:
            return age

    # checks that the half-elf is at least medium hight
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

    def setDarkvision(self, darkvision: int):
        self.darkvision = darkvision

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
            print("Height not a medium creature. A half-elf is a medium creature between 5 ft and 6 ft, but medium creatures are between 4 ft and 8 ft")
            super().setHeight(60)

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




