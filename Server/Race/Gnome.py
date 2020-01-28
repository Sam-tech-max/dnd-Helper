import Race as r
import Stats as s
import SpellBook
import Spell
from typing import List

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
        gnomeCunning = "gnome cunning: You have advantage on all Intelligence, Wisdom, and Charisma saving throws aginst magic"
        self.featuresAndTraits = [gnomeCunning]
        if(subrace == "forest"):
            minorIllusion = Spell.Spell(0, "minor illusion",
                                        "1 action", "1 minute",
                                        "30 ft(5 ft cube)",
                                        "illusion", "none",
                                        "S, M (a bit of fleece)",
                                        "control",
                                        "You create a sound or an image of an object within range that lasts for the duration. The illusion also ends if you dismiss it as an action or cast this spell again. If you create a sound, its volume can range from a whisper to a scream. It can be your voice, someone else's voice, a lion's roar, a beating of drums, or any other sound you choose. The sound continues unabated throughout the duration, or you can make discrete sounds at different times before the spell ends. If you create an image of an object--such as a chair, muddy footprints, or a small chest--it must be no larger than a 5-foot cube. The image can't create sound, light, smell, or any other sensory effect. Physical interaction with the image reveals it to be an illusion, because things can pass through it. If a creature uses its action to examine the sound or image, the creature can determine that it is an illusion with a successful Intelligence (Investigation) check against your spell save DC. If a creature discerns the illusion for what it is, the illusion becomes faint to the creature.")
            self.spellBook = SpellBook.SpellBook(1, 86400, 0, 0, 0, 0, 0, 0, 0, 0, 0,[minorIllusion])
            self.spellCastingModifier = "intelligence"
            self.hasSpellBook = True
            self.featuresAndTraits.append("speak with small beasts: Through sounds and gestures you can communicate simple ideas with Small or smaller beasts. Forest gnomes love animals and often keep squirrels, badgers, rabbits, moles, woodpeckers, and other creatures as beloved pets.")
        elif(subrace == "rock"):
            self.featuresAndTraits.append("artificer's lore: Whenever you make an Intelligence (History) check related to magic items, alchemical objects, or technological devices, you can add twice your proficiency bonus, instead of any proficiency bonus you normally apply.")
            self.featuresAndTraits.append("Tinker: You have proficiency with artisan’s tools (tinker’s tools). Using those tools, you can spend 1 hour and 10 gp worth of materials to construct a Tiny clock work device (AC 5, 1 hp). The device ceases to function after 24 hours (unless you spend 1 hour repairing it to keep the device functioning), or when you use your action to dismantle it; at that time, you can reclaim the materials used to create it. You can have up to three such devices active at a time. When you create a device, choose one of the following options; Clockwork Toy: This toy is a clock work animal, monster, or person, such as a frog, mouse, bird, dragon, or soldier. When placed on the ground, the toy moves 5 feet across the ground on each of your turns in a random direction. It makes noises as appropriate to the creature it represents. Fire Starter. The device produces a miniature flame, which you can use to light a candle, torch, or campfire. Using the device requires your action; Music Box: When opened, this music box plays a single song at a moderate volume. The box stops playing when it reaches the song’s end or when it is closed.")
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
        self.printFeaturesAndTraits()
        if(self.hasSpellBook):
            self.getSpellBook().printSpellBook()

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

    def getFeaturesAndTraits(self) -> List[str]:
        return self.featuresAndTraits

    def setFeaturesAndTraits(self, featuresAndTraits: List[str]):
        self.featuresAndTraits = featuresfeaturesAndTraits

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

    def getSpellBook(self) -> List[Spell.Spell]:
        return self.spellBook

    def setSpellBook(self, spellBook: Spell.Spell):
        self.spellBook = spellBook

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




