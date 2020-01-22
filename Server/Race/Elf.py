import Race as r
import Stats as s

class Elf(r.Race):
    def __init__(self, age: int=100, alignment: str="chaotic good",
                 height: int=60, stats: s.Stats=s.Stats(),
                 subrace: str="high", weight: int=120):
        subrace = subrace.lower()
        wisPer = stats.getStat("wisdom: perception")
        wisPer.setHasProficiency(True)
        stats.setStat(wisPer)
        if(subrace == "dark"):
            super().__init__("elf", age, alignment, height, "common elvish", "medium", stats, 30, subrace, weight)
            self.darkvision = 120
        elif(subrace == "wood"):
            super().__init__("elf", age, alignment, height, "common elvish", "medium", stats, 35, subrace, weight)
            self.darkvision = 60
        else:
            l = r.chooseLanguage()
            super().__init__("elf", age, alignment, height, "common elvish" + l, "medium", stats, 30, "high", weight)
            self.darkvision = 60

#//----------// //----------// //----------//
# Other methods associatied with the Elf race
#//----------// //----------// //----------//
    def abilityScoreIncrease(self):
        stats = self.getStats()
        print("Your Dexterity score increases by 2.")
        dex = stats.getStat("dexterity")
        dex.setScore(dex.getScore() + 2)
        stats.setStat(dex)
        if(super().getSubrace() == "dark"):
            print("Your Charisma score increases by 1")
            cha = stats.getStat("charisma")
            cha.setScore(cha.getScore() + 1)
            stats.setStat(cha)
        elif(super().getSubrace() == "high"):
            print("Your Intelligence score increases by 1.")
            intell = stats.getStat("intelligence")
            intell.setScore(intell.getScore() + 1)
            stats.setStat(intell)
        elif(super().getSubrace() == "wood"):
            print("Your Wisdom score increases by 1")
            wis = stats.getStat("wisdom")
            wis.setScore(wis.getScore() + 1)
            stats.setStat(wis)
        super().setStats(stats)

#//----------// //----------// //----------//
# Print methods:
# These methods will print out all of the
# variables.
#//----------// //----------// //----------//
    def printElf(self, showStats: bool):
        super().printRace(showStats)
        print("Darkvision:", self.getDarkvision())

#//----------// //----------// //----------//
# Check methods:
# These methods will give a boolean value.
#//----------// //----------// //----------//
    def checkAge(self, age: int) -> int:
        if(age < 0):
            print("You are too young. Setting age to 100.")
            return 100
        elif(age > 750):
            print("You are too old. Setting age to 750.")
            return 750
        else:
            return age

    # checks that the elf is at least medium hight
    # which is 48 in to 96 ft
    def checkHeight(self, height: int) -> bool:
        if(height >= 48 and height <= 96):
            return True
        else:
            return False

    def checkSubrace(self, subrace: str) -> bool:
        subrace = subrace
        if(subrace == "dark" or subrace == "high" or subrace == "wood"):
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
        if(not self.checkHeight(self.height)):
            self.setHeight(60)
        return self.height

    def setHeight(self, height: int):
        if(self.checkHeight(height)):
            super().setHeight(height)
        else:
            print("Height not a medium creature. A elf is a medium creature between 5 ft and 6 ft, but medium creatures are between 4 ft and 8 ft")
            super().setHeight(60)

    def getSubrace(self) -> str:
        if(self.checkSubrace(self.subrace)):
            return self.subrace
        else:
            self.setSubrace("high")
            return self.subrace

    def setSubrace(self, subrace: str):
        if(not self.checkSubrace(subrace)):
            subrace = "high"
        self.subrace = subrace

#//----------// //----------// //----------//
# Main Class
#//----------// //----------// //----------//
e = Elf()
e.printElf(False)
e.abilityScoreIncrease()
e.printElf(False)




