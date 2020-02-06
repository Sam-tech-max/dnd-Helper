import Races.Race as r
import Stats as s
import Spell
import SpellBook

class Tiefling(r.Race):
    def __init__(self, age: int=16, alignment: str="chaotic evil",
                 height: int=60, stats: s.Stats=s.Stats(),
                 weight: int=150, gender: str="male",
                 firstName: str="akmenos", lastName: str="art"):
        super().__init__("tiefling", age, alignment, height,
                         "common infernal", "medium", stats, 30,
                         "none", weight, gender, firstName, lastName)
        self.darkvision = 60
        self.resistance = "fire damage"
        thaumaturgy = Spell.Spell(0, "thaumaturgy", "1 action",
                                  "Up to 1 minute", "30 ft",
                                  "transmutation", "none", "V",
                                  "control",
                                  "You manifest a minor wonder, a sign of supernatural power, within range. You create one of the following magical effects within range: Your voice booms up to three times as loud as normal for 1 minute; You cause flames to flicker, brighten, dim, or change color for 1 minute; You cause harmless tremors in the ground for 1 minute; You create an instantaneous sound that originates from a point of your choice within range, such as a rumble of thunder, the cry of a raven, or ominous whispers; You instantaneously cause an unlocked door or window to fly open or slam shut; You alter the appearance of your eyes for 1 minute. If you cast this spell multiple times, you can have up to three of its 1-minute effects active at a time, and you can dismiss such an effect as an action.")
        self.spellBook = SpellBook.SpellBook(1, 86400, 0, 0, 0, 0, 0,
                                             0, 0, 0, 0,[thaumaturgy])
        self.hasSpellBook == True
        self.spellCastingModifier = "charisma"


#//----------// //----------// //----------//
# Other methods associatied with the Human race
#//----------// //----------// //----------//
    def abilityScoreIncrease(self):
        stats = self.getStats()
        print("Your Charisma score increases by 2")
        cha = stats.getStat("charisma")
        cha.setScore(cha.getScore() + 2)
        stats.setStat(cha)

        print("Your Intelligence score increases by 1.")
        intell = stats.getStat("intelligence")
        intell.setScore(intell.getScore() + 1)
        stats.setStat(intell)

        super().setStats(stats)

    def levelUp(self, level:int):
        if(level == 3):
            print("You now can cast hellish rebuke once per day")
            hellishRebuke = Spell.Spell(1, "hellish rebuke",
                                        "1 reaction",
                                        "instantaneous", "60 ft",
                                        "evocation", "DEX save",
                                        "V, S", "fire",
                                        "You point your finger, and the creature that damaged you is momentarily surrounded by hellish flames. The creature must make a Dexterity saving throw. It takes 2d10 fire damage on a failed save, or half as much damage on a successful one. At Higher Levels. When you cast this spell using a spell slot of 2nd level or higher, the damage increases by 1d10 for each slot level above 1st.")
            self.getSpellBook().addSpell(hellishRebuke)
            self.getSpellBook().setSpellSlot(1, 1)
        elif(level == 5):
            print("You now can cast darkness once per day")
            darkness = Spell.Spell(2, "darkness", "1 action",
                                   "10 minutes",
                                   "60 ft (15 ft sphere)",
                                   "evocation", "none",
                                   "V, M (bat fure and a drop of pitch or piece of coal)",
                                   "control",
                                   "Magical darkness spreads from a point you choose within range to fill a 15-foot-radius sphere for the duration. The darkness spreads around corners. A creature with darkvision can't see through this darkness, and nonmagical light can't illuminate it. If the point you choose is on an object you are holding or one that isn't being worn or carried, the darkness emanates from the object and moves with it. Completely covering the source of the darkness with an opaque object, such as a bowl or a helm, blocks the darkness. If any of this spell's area overlaps with an area of light created by a spell of 2nd level or lower, the spell that created the light is dispelled.")
            self.getSpellBook().addSpell(darkness)
            self.getSpellBook().setSpellSlot(2, 1)
        else:
            print("Nothing happens for teifling at this level.")


#//----------// //----------// //----------//
# Print methods:
# These methods will print out all of the
# variables.
#//----------// //----------// //----------//
    def printRace(self, showStats: bool):
        super().printRace(showStats)
        print("Darkvision:", self.getDarkvision(), "ft")
        print("Resistance:", self.getResistance())
        self.getSpellBook().printSpellBook()


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

    def getResistance(self) -> str:
        return self.resistance

    def setResistance(self, resistance: str):
        self.resistance = resistance

    def getSpellBook(self) -> SpellBook.SpellBook:
        return self.spellBook

    def setSpellBook(self, spellBook: SpellBook.SpellBook):
        self.spellBook = spellBook


#//----------// //----------// //----------//
# Main Class
#//----------// //----------// //----------//





