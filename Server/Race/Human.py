import Race as r
import Stats as s

class Human(r.Race):
    def __init__(self, age: int=16, alignment: str="true neutral",
                 height: int=60, stats: s.Stats=s.Stats(),
                 subrace: str="calishite", weight: int=150):
        subrace = subrace.lower()
        l = r.chooseLanguage()
        super().__init__("human", age, alignment, height, "common" + l, "medium", stats, 30, subrace, weight)


#//----------// //----------// //----------//
# Other methods associatied with the Human race
#//----------// //----------// //----------//
    def abilityScoreIncrease(self):
        stats = self.getStats()
        print("Your Dexterity score increases by 1.")
        dex = stats.getStat("dexterity")
        dex.setScore(dex.getScore() + 1)
        stats.setStat(dex)

        print("Your Charisma score increases by 1")
        cha = stats.getStat("charisma")
        cha.setScore(cha.getScore() + 1)
        stats.setStat(cha)

        print("Your Intelligence score increases by 1.")
        intell = stats.getStat("intelligence")
        intell.setScore(intell.getScore() + 1)
        stats.setStat(intell)

        print("Your Wisdom score increases by 1")
        wis = stats.getStat("wisdom")
        wis.setScore(wis.getScore() + 1)
        stats.setStat(wis)

        print("Your Strength score increases by 1")
        strength = stats.getStat("strength")
        strength.setScore(strength.getScore() + 1)
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
    def printHuman(self, showStats: bool):
        super().printRace(showStats)

#//----------// //----------// //----------//
# Check methods:
# These methods will give a boolean value.
#//----------// //----------// //----------//
    def checkAge(self, age: int) -> int:
        if(age < 0):
            print("You are too young. Setting age to 16.")
            return 16
        elif(age > 100):
            print("You are too old. Setting age to 100.")
            return 100
        else:
            return age

    # checks that the human is at least medium hight
    # which is 48 in to 96 ft
    def checkHeight(self, height: int) -> bool:
        if(height >= 48 and height <= 96):
            return True
        else:
            return False

    def checkSubrace(self, subrace: str) -> bool:
        subrace = subrace
        if(subrace == "calishite" or subrace == "chondathan" or
           subrace == "damaran" or subrace == "issuskan" or
           subrace == "mulan" or subrace == "rashemi" or
           subrace == "shou" or subrace == "tethyrian" or
           subrace == "turami"):
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

    def getHeight(self) -> int:
        if(not self.checkHeight(self.height)):
            self.setHeight(60)
        return self.height

    def setHeight(self, height: int):
        if(self.checkHeight(height)):
            super().setHeight(height)
        else:
            print("Height not a medium creature. A human is a medium creature between 5 ft and 6 ft, but medium creatures are between 4 ft and 8 ft")
            super().setHeight(60)

    def getSubrace(self) -> str:
        if(self.checkSubrace(self.subrace)):
            return self.subrace
        else:
            self.setSubrace("calishite")
            return self.subrace

    def setSubrace(self, subrace: str):
        if(not self.checkSubrace(subrace)):
            subrace = "calishite"
        self.subrace = subrace

#//----------// //----------// //----------//
# Main Class
#//----------// //----------// //----------//
h = Human()
h.printHuman(False)
h.abilityScoreIncrease()
h.printHuman(False)




