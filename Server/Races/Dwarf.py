import Races.Race as r
import Stats as s

def chooseToolProficiency(toolName: str = "empty") -> str:
    toolName = toolName.lower()
    if(toolName == "smith's tools" or toolName == "brewer's supplies" or toolName == "mason's tools"):
        return toolName
    else:
        print("Choose from the following tools:")
        toolname = str(input("smith's tools; brewer's supplies; or mason's tools: "))
        chooseToolProficiency(toolname)


class Dwarf(r.Race):
    def __init__(self, age: int=50, alignment: str="lawful good",
                 height: int=48, stats: s.Stats=s.Stats(),
                 subrace: str="hill", weight: int=150,
                 gender: str="male", firstName: str="Adrik",
                 lastName: str="Balderk"):
        super().__init__("dwarf", age, alignment, height,
                         "common dwarvish", "medium", stats, 25,
                         subrace, weight, gender, firstName,
                         lastName)
        self.darkvision = 60
        self.featuresAndTraits = ["dwarven resilience: You have advantage on saving throws against poison, and you have resistance against poison damage."]
        tp = "tool proficiency: " + str(chooseToolProficiency())
        self.otherProficiencies = ["dwarven combat training: You have proficiency with the battleaxe, handaxe, throwing hammer, and warhammer.",
                                   tp,
                                   "stonecunning: Whenever you make an Intelligence (History) check related to the origin of stone work, you are considered proficient in the History skill and add double your proficiency bonus to the check, instead of your normal proficiency bonus."]
        if(subrace == "mountain"):
            self.otherProficiencies.append("dwarven armor training: You have proficiency with light and medium armor.")


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
            wis = stats.getStat("wisdom")
            wis.setScore(wis.getScore() + 1)
            stats.setStat(wis)
        elif(super().getSubrace() == "mountain"):
            print("Your Strength score increases by 2")
            strength = stats.getStat("strength")
            strength.setScore(strength.getScore() + 2)
            stats.setStat(strength)
        super().setStats(stats)

#//----------// //----------// //----------//
# Print methods:
# These methods will print out all of the
# variables.
#//----------// //----------// //----------//
    def printRace(self, printStats: bool):
        super().printRace(printStats)
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
