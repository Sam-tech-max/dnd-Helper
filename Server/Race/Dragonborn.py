import Race as r
import Stats as s

class Dragonborn(r.Race):
    def __init__(self, age: int=15, alignment: str="lawful good",
                 height: int=72, stats: s.Stats=s.Stats(),
                 subrace: str="black", weight: int=250):
        subrace = subrace.lower()
        super().__init__("dragonborn", age, alignment, height, "common draconic", "medium", stats, 30, subrace, weight)


#//----------// //----------// //----------//
# Other methods associatied with the Human race
#//----------// //----------// //----------//
    def abilityScoreIncrease(self):
        stats = self.getStats()
       
        print("Your Charisma score increases by 1")
        cha = stats.getStat("charisma")
        cha.setScore(cha.getScore() + 1)
        stats.setStat(cha)

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
    def printDragonborn(self, showStats: bool):
        super().printRace(showStats)

#//----------// //----------// //----------//
# Check methods:
# These methods will give a boolean value.
#//----------// //----------// //----------//
    def checkAge(self, age: int) -> int:
        if(age < 0):
            print("You are too young. Setting age to 16.")
            return 15
        elif(age > 80):
            print("You are too old. Setting age to 80.")
            return 80
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
        subrace = subrace.lower()
        if(subrace == "black" or subrace == "blue" or
           subrace == "brass" or subrace == "branze" or
           subrace == "copper" or subrace == "gold" or
           subrace == "green" or subrace == "red" or
           subrace == "silver" or subrace == "white"):
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
            print("Height not a medium creature. A Dragonborn is a medium creature between 5 ft and 6 ft, but medium creatures are between 4 ft and 8 ft")
            super().setHeight(60)

    def getSubrace(self) -> str:
        if(self.checkSubrace(self.subrace)):
            return self.subrace
        else:
            self.setSubrace("black")
            return self.subrace

    def setSubrace(self, subrace: str):
        if(not self.checkSubrace(subrace)):
            subrace = "black"
        self.subrace = subrace

#//----------// //----------// //----------//
# Main Class
#//----------// //----------// //----------//
d = Dragonborn()
d.printDragonborn(False)
d.abilityScoreIncrease()
d.printDragonborn(False)




