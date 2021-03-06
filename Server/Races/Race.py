import Races.Stats as s

def chooseLanguage(l: str = "empty")->str:
    l = l.lower()
    if (l == "abyssal" or l == "aquan" or l == "auran" or
             l == "celestial" or l == "common" or l == "deep" or
             l == "draconic" or l == "druidic" or l == "dwarvish" or
             l == "elvish" or l == "giant" or l == "gnomish" or
             l == "goblin" or l == "gnoll" or l == "halfling" or
             l == "ignan" or l == "infernal" or l == "orc" or
             l == "primordial" or l == "sylvan" or l == "terran" or
             l == "undercommon"):
        return " " + l
    else:
        print("Please choose from the following languages:")
        l = str(input("abyssal, aquan, auran, celestial, common, deep, draconic, druidic, dwarvish elvish, giant, gnomish, goblin, gnoll, halfling, ignan, infernal, orc, primordial, sylvan, terran, or undercommon: "))
        return chooseLanguage(l)

def chooseStat(s: str = "empty")->str:
    s = s.lower()
    if (s == "strength" or s == "dexterity" or s == "constitution" or
        s == "intelligence" or s == "wisdom" or s == "charisma"):
        return s
    else:
        print("Please choose from the following stats to improve:")
        s = str(input("strength, dexterity, constitution, intelligence, wisdom or charisma: "))
        return chooseStat(s)

class Race(object):
    def __init__(self, race: str="", age: int=0,
                 alignment: str="true neutral", height: int=0,
                 languages:str="empty", size: str="tiny",
                 stats: s.Stats=s.Stats(), speed: int=30,
                 subrace: str=" ", weight: int=0, gender: str="male",
                 firstName: str="", lastName: str=""):
        self.age = age
        self.alignment = alignment.lower()
        self.firstName = firstName.lower()
        self.gender = gender.lower()
        self.hasSpellBook = False
        self.height = height
        self.languages = languages.lower()
        self.lastName = lastName.lower()
        self.size = size.lower()
        self.stats = stats
        self.speed = speed
        self.subrace = subrace.lower()
        self.race = race.lower()
        self.weight = weight

#//----------// //----------// //----------//
# Print methods:
# These methods will print out all of the
# variables.
#//----------// //----------// //----------//
    def printRace(self, printStat: bool=True):
        print("Character Name:", self.getFirstName(),
              self.getLastName())
        print("Race:", self.getRace())
        print("Gender:", self.getGender())
        print("Age:", self.getAge())
        print("Alignment:",self.getAlignment())
        print("Size:",self.getSize())
        print("Height:", self.getHeight(), "in")
        print("Weight:", self.getWeight(), "lb")
        print("Speed:",self.getSpeed())
        print("Languages:",self.getLanguages())
        print("Subrace:",self.getSubrace())
        if(printStat):
            self.getStats().printStats()


#//----------// //----------// //----------//
# Check methods:
# These methods will give a boolean value.
#//----------// //----------// //----------//
    def checkAlignment(self, alignment: str="empty")-> bool:
        a = alignment.lower()
        if(a == "empty"):
            print("empty")
            return False
        elif(a == "lawful good" or a == "lawful neutral"or
             a == "lawful evil" or a == "neutral good" or
             a == "true neutral" or a == "neutral evil" or
             a == "chaotic good" or a == "chaotic neutral" or
             a == "chaotic evil"):
            return True
        else:
            return False

    def checkGender(self, gender: str="empty") -> bool:
        g = gender.lower()
        if(g == "empty"):
            print("empty")
            return False
        elif(g == "female" or g == "male"):
            return True
        else:
            return False

    def checkLanguage(self, language: str="empty") -> bool:
        l = language.lower()
        if(l == "empty"):
            print("empty")
            return False
        elif(l == "abyssal" or l == "aquan" or l == "auran" or
             l == "celestial" or l == "common" or l == "deep" or
             l == "draconic" or l == "druidic" or l == "dwarvish" or
             l == "elvish" or l == "giant" or l == "gnomish" or
             l == "goblin" or l == "gnoll" or l == "halfling" or
             l == "ignan" or l == "infernal" or l == "orc" or
             l == "primordial" or l == "sylvan" or l == "terran" or
             l == "undercommon"):
            return True
        else:
            return False

    def checkAllLanguages(self):
        langs = self.languages.split()
        langs = list(dict.fromkeys(langs))
        langs.sort()
        newLangs = ""
        for l in langs:
            if(self.checkLanguage(l)):
                newLangs += l + " "
        self.languages = newLangs

    def checkSize(self, size: str="empty")-> bool:
        s = size.lower()
        if(s == "empty"):
            print("empty")

        elif(s == "tiny" or s == "small" or s == "medium" or
             s == "large" or s == "huge" or s == "gargantuan"):
            return True
        else:
            return False

#//----------// //----------// //----------//
# Get and Set methods
#//----------// //----------// //----------//
    def getRace(self) -> str:
        return self.race

    def setRace(self, race: str):
        self.race = race.lower()

    def getAge(self) -> int:
        return self.age

    def setAge(self, age: int):
        self.age = age

    def getAlignment(self) -> str:
        return self.alignment

    def setAlignment(self, alignment: str):
        if self.checkAlignment(alignment):
            self.alignment = alignment.lower()
        elif(not self.checkAlignment(self.getAlignment())):
            self.alignment = "true neutral"

    def getGender(self) -> str:
        return self.gender

    def setGender(self, gender: str):
        if(self.checkGender()):
            self.gender = gender
        elif(self.checkGender(self.getGender())):
            print("Not male or Female for gender.")
        else:
            self.gender = "male"
            print("Set gender to male.")

    def getFirstName(self) -> str:
        return self.firstName

    def setFirstName(self, firstName: str):
        self.firstName = firstName

    def getLastName(self) -> str:
        return self.lastName

    def setLastName(self, lastName: str):
        self.lastName = lastName

    def getSize(self) -> str:
        return self.size

    def setSize(self, size: str):
        if self.checkSize(size):
            self.size = size.lower()
        elif(not self.checkSize(self.getSize())):
            self.size = "tiny"

    def getStats(self) -> s.Stats:
        return self.stats

    def setStats(self, stats: s.Stats):
        self.stats = stats

    def getSpeed(self) -> int:
        return self.speed

    def setSpeed(self, speed: int):
        self.speed = speed

    def getLanguages(self) -> str:
        self.checkAllLanguages()
        return self.languages

    def setLanguages(self, languages:str):
        self.checkAllLanguages()
        self.languages = languages.lower()

    def addALanguage(self, language:str="empty"):
        self.checkAllLanguages()
        if(self.checkLanguage(language)):
            langs = self.getLanguages()
            langs += " " + language
            self.setLanguages(langs)
        else:
            print("Not a Language")

    def getSubrace(self) -> str:
        return self.subrace.lower()

    def setSubrace(self, subrace: str):
        self.subrace = subrace.lower()

    def getHeight(self) -> int:
        return self.height

    def setHeight(self, height:int):
        self.height = height

    def getWeight(self) -> int:
        return self.weight

    def setWeight(self, weight: int):
        self.weight = weight


#//----------// //----------// //----------//
# Main Class
#//----------// //----------// //----------//
