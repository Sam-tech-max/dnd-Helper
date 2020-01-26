import Race as r
import Stats as s

class Gnome(r.Race):
    def __init__(self, age: int=40, alignment: str="neutral good",
                 height: int=36, stats: s.Stats=s.Stats(),
                 subrace: str="forest", weight: int=40,
                 gender: str="male", firstName: str="alston",
                 lastName: str="beren", nickName: str="aleslosh"):
        subrace = subrace.lower()
        super().__init__("Gnome", age, alignment, height,
                         "common gnomish", "small", stats, 25,
                         subrace, weight, gender, firstName,
                         lastName)
        self.darkvision = 60
        self.nickName = nickName.lower()


#//----------// //----------// //----------//
# Other methods associatied with the Human race
#//----------// //----------// //----------//
    def abilityScoreIncrease(self):
        stats = self.getStats()
        print("Your Intelligence score increases by 2.")
        intell = stats.getStat("intelligence")
        intell.setScore(intell.getScore() + 2)
        stats.setStat(intell)
        if(self.getSubrace() == "forest"):
            print("Your Dexterity score increases by 1.")
            dex = stats.getStat("dexterity")
            dex.setScore(dex.getScore() + 1)
            stats.setStat(dex)
        elif(self.getSubrace() == "rock"):
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
        print("NickName:", self.getNickName())
        super().printRace(showStats)
        print("Darkvision:", self.getDarkvision(), "ft")

#//----------// //----------// //----------//
# Check methods:
# These methods will give a boolean value.
#//----------// //----------// //----------//
    def checkAge(self, age: int) -> int:
        if(age < 0):
            print("You are too young. Setting age to 40.")
            return 40
        elif(age > 500):
            print("You are too old. Setting age to 500.")
            return 500
        else:
            return age

    # checks that the human is at least medium hight
    # which is 48 in to 96 ft
    def checkHeight(self, height: int) -> bool:
        if(height >= 24 and height <= 48):
            return True
        else:
            return False

    def checkSubrace(self, subrace: str) -> bool:
        subrace = subrace
        if(subrace == "forest" or subrace == "rock"):
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
        if(darkvision >= 0):
            self.darkvision = darkvision
        else:
            self.darkvision = 0

    def getHeight(self) -> int:
        if(not self.checkHeight(self.height)):
            self.setHeight(60)
        return self.height

    def setHeight(self, height: int):
        if(self.checkHeight(height)):
            super().setHeight(height)
        else:
            print("Height not for a small creature. A gnome is a small creature between 2 ft and 4 ft")
            super().setHeight(36)

    def getNickName(self) -> str:
        return self.nickName

    def setNickName(self, nickName: str):
        self.nickName = nickName

    def getSubrace(self) -> str:
        if(self.checkSubrace(self.subrace)):
            return self.subrace
        else:
            self.setSubrace("forest")
            return self.subrace

    def setSubrace(self, subrace: str):
        if(not self.checkSubrace(subrace)):
            subrace = "forest"
        self.subrace = subrace

#//----------// //----------// //----------//
# Main Class
#//----------// //----------// //----------//
g = Gnome()
g.printRace(False)
g.abilityScoreIncrease()
g.printRace(False)




