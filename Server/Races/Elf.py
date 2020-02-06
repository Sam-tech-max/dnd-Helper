import Races.Race as r
import Stats as s
import SpellBook
import Spell
from typing import List

def chooseWizardCantrip(spellName: str = "empty")->Spell.Spell:
    spellName = spellName.lower()
    if (spellName == "acid splash"):
        return makeCantrip("acid splash")
    elif(spellName == "blade ward"):
        return makeCantrip("blade ward")
    elif(spellName == "chill touch"):
        return makeCantrip("chill touch")
    elif(spellName == "dancing lights"):
        return makeCantrip("dancing lights")
    elif(spellName == "fire bolt"):
        return makeCantrip("fire bolt")
    elif(spellName == "friends"):
        return makeCantrip("friends")
    elif(spellName == "light"):
        return makeCantrip("light")
    elif(spellName == "mage hand"):
        return makeCantrip("mage hand")
    elif(spellName == "mending"):
        return makeCantrip("mending")
    elif(spellName == "message"):
        return makeCantrip("message")
    elif(spellName == "minor illusion"):
        return makeCantrip("minor illusion")
    elif(spellName == "poison spray"):
        return makeCantrip("poison spray")
    elif(spellName == "prestidigitation"):
        return makeCantrip("prestidigitation")
    elif(spellName == "ray of frost"):
        return makeCantrip("ray of frost")
    elif(spellName == "shocking grasp"):
        return makeCantrip("shocking grasp")
    elif(spellName == "true strike"):
        return makeCantrip("true strike")
    else:
        print("Please choose from the following languages:")
        spellName = str(input("acid splash, blade ward, chill touch, dancing lights, fire bolt, friends, light, mage hand, mending, message, minor illusion, poison spray, prestidigitation, ray of frost, shocking grasp, true strike: "))
        return chooseWizardCantrip(spellName)

def makeCantrip(spellName: str = "empty") -> Spell.Spell:
    if(spellName == "acid splash"):
        return Spell.Spell(0, "acid splash", "1 action", "instantaneous", "60 ft", "conjuration", "DEX save", "V, S", "acid", "You hurl a bubble of acid. Choose one or two creatures you can see within range. If you choose two, they must be within 5 feet of each other. A target must succeed on a Dexterity saving throw or take 1d6 acid damage. This spell’s damage increases by 1d6 when you reach 5th level (2d6), 11th level (3d6), and 17th level (4d6).")
    elif(spellName == "blade ward"):
        return Spell.Spell(0, "blade ward", "1 action", "1 round", "self", "abjuration", "none", "V, S", "control", "You extend your hand and trace a sigil of warding in the air. Until the end of your next turn, you have resistance against bludgeoning, piercing, and slashing damage dealt by weapon attacks.")
    elif(spellName == "chill touch"):
        return Spell.Spell(0, "chill touch", "1 action", "1 round", "120 ft", "necromancy", "ranged", "V, S", "necrotic", "You create a ghostly, skeletal hand in the space of a creature within range. Make a ranged spell attack against the creature to assail it with the chill of the grave. On a hit, the target takes 1d8 necrotic damage, and it can't regain hit points until the start of your next turn. Until then, the hand clings to the target. If you hit an undead target, it also has disadvantage on attack rolls against you util the end of your next turn. This spell's damage increases by 1d8 when you reach 5th level (2d8), 11th level (3d8), and 17th level (4d8).")
    elif(spellName == "dancing lights"):
        return Spell.Spell(0, "dancing lights", "1 action", "1 minute","120 ft", "evocation", "none", "V, S, M (a bit of phosphorus or wychwood, or a glowworm)", "utility", "You create up to four torch-sized lights within range, making them appear as torches, lanterns, or glowing orbs that hover in the air for the duration. You can also combine the four lights into one glowing vaguely humanoid form of Medium size. Whichever form you choose, each light sheds dim light in a 10-foot radius. As a bonus action on your turn, you can move the lights up to 60 feet to a new spot within range. A light must be within 20 feet of another light created by this spell, and a light winks out if it exceeds the spell's range.")
    elif(spellName == "fire bolt"):
        return Spell.Spell(0, "fire bolt", "1 action", "instantaneous", "120 ft", "evocation", "ranged", "V, S", "fire", "You hurl a mote of fire at a creature or object within range. Make a ranged spell attack against the target. On a hit, the target takes 1d10 fire damage. A flammable object hit by this spell ignites if it isn't being worn or carried. This spell's damage increases by 1d10 when you reach 5th level (2d10), 11th level (3d10), and 17th level (4d10).")
    elif(spellName == "friends"):
        return Spell.Spell(0, "friends", "1 action", "1 minute", "self", "enchantment", "none", "S, M (a small amount of makeup applied to the face as the spell is cast)", "control", "For the duration, you have advantage on all Charisma checks directed at one creature of your choice that isn’t hostile toward you. When the spell ends, the creature realizes that you used magic to influence its mood and becom es hostile toward you. A creature prone to violence might attack you. Another creature might seek retribution in other ways (at the DM ’s discretion), depending on the nature of your interaction with it.")
    elif(spellName == "light"):
        return Spell.Spell(0, "light", "1 action", "1 hour", "touch (20 ft sphere)", "evocation", "dex save", "V, M (a firefly or phosphorescent)", "creation", "You touch one object that is no larger than 10 feet in any dimension. Until the spell ends, the object sheds bright light in a 20-foot radius and dim light for an additional 20 feet. The light can be colored as you like. Completely covering the object with something opaque blocks the light. The spell ends if you cast it again or dismiss it as an action. If you target an object held or w orn by a hostile creature, that creature must succeed on a Dexterity saving throw to avoid the spell.")
    elif(spellName == "mage hand"):
        return Spell.Spell(0, "mage hand", "1 action", "1 minute", "1 minute", "conjuration", "none", "V, S, M (a piece of cured leather)", "utility", "A spectral, floating hand appears at a point you choose within range. The hand lasts for the duration or until you dismiss it as an action. The hand vanishes if it is ever more than 30 feet away from you or if you cast this spell again. You can use your action to control the hand. You can use the hand to manipulate an object, open an unlocked door or container, stow or retrieve an item from an open container, or pour the contents out of a vial. You can move the hand up to 30 feet each time you use it. The hand can’t attack, activate magic items, or carry more than 10 pounds.")
    elif(spellName == "mending"):
        return Spell.Spell(0, "mending", "1 minute", "instantaneous", "touch", "transmutation", "none", "V, S, M (two lodestones)", "utility", "This spell repairs a single break or tear in an object you touch, such as a broken chain link, two halves of a broken key, a torn cloak, or a leaking wineskin. As long as the break or tear is no larger than 1 foot in any dimension, you mend it. leaving no trace of the former damage. This spell can physically repair a magic item or construct, but the spell can’t restore magic to such an object.")
    elif(spellName == "message"):
        return Spell.Spell(0, "message", "1 action", "1 round", "120 ft", "transumutation", "none", "V, S, M (a short piece of copper wire)", "communication", "You point your finger toward a creature within range and whisper a message. The target (and only the target) hears the message and can reply in a whisper that only you can hear. You can cast this spell through solid objects if you are familiar with the target and know it is beyond the barrier. Magical silence. 1 foot of stone, 1 inch of common metal, a thin sheet of lead, or 3 feet of wood blocks the spell. The spell doesn’t have to follow a straight line and can travel freely around corners or through openings.")
    elif(spellName == "minor illusion"):
        return Spell.Spell(0, "minor illusion", "1 action", "1 minute", "30 ft", "illusion", "none", "S, M(a bit of fleece)", "control", "You create a sound or an image of an object within range that lasts for the duration. The illusion also ends if you dismiss it as an action or cast this spell again. If you create a sound, its volume can range from a whisper to a scream . It can be your voice, someone else’s voice, a lion’s roar, a beating of drums, or any other sound you choose. The sound continues unabated throughout the duration, or you can make discrete sounds at different times before the spell ends. If you create an im age of an object—such as a chair, muddy footprints, or a small chest—it must be no larger than a 5-foot cube. The image can’t create sound, light, smell, or any other sensory effect. Physical interaction with the image reveals it to be an illusion, because things can pass through it. If a creature uses its action to examine the sound or image, the creature can determine that it is an illusion with a successful Intelligence (Investigation) check against your spell save DC. If a creature discerns the illusion for what it is, the illusion becomes faint to the creature.")
    elif(spellName == "poison spray"):
        return Spell.Spell(0, "poison spray", "1 action", "instantaneous", "10 ft", "conjuration", "con save", "V, S", "poison", "You extend your hand toward a creature you can see within range and project a puff of noxious gas from your palm. The creature must succeed on a Constitution saving throw or take 1d12 poison damage. This spell’s damage increases by 1d12 when you reach 5th level (2d12), 11th level (3d12), and 17th level (4d12).")
    elif(spellName == "prestidigitation"):
        return Spell.Spell(0, "prestidigitation", "1 action", "1 hour", "10 ft", "transmutation", "none", "V, S", "utility", "This spell is a minor magical trick that novice spellcasters use for practice. You create one of the following magical effects within range: You create an instantaneous, harmless sensory effect, such as a shower of sparks, a puff of wind, faint musical notes, or an odd odor; You instantaneously light or snuff out a candle, a torch, or a small campfire; You instantaneously clean or soil an object no larger than 1 cubic foot; You chill, warm, or flavor up to 1 cubic foot of nonliving material for 1 hour; You make a color, a small mark, or a symbol appear on an object or a surface for 1 hour; or You create a nonmagical trinket or an illusory image that can fit in your hand and that lasts until the end of your next turn. If you cast this spell multiple times, you can have up to three of its non-instantaneous effects active at a time, and you can dismiss such an effect as an action.")
    elif(spellName == "ray of frost"):
        return Spell.Spell(0, "ray of frost", "1 action", "instantaneous", "60 ft", "evocation", "ranged", "V, S", "cold", "A frigid beam o f blue-white light streaks toward a creature within range. Make a ranged spell attack against the target. On a hit, it takes 1d8 cold damage, and its speed is reduced by 10 feet until the start of your next turn. The spell’s damage increases by 1d8 when you reach 5th level (2d8), 11th level (3d8), and 17th level (4d8).")
    elif(spellName == "shocking grasp"):
        return Spell.Spell(0, "shocking grasp", "1 action", "instantaneous", "touch", "evocation", "melee", "V, S", "lightning", "Lightning springs from your hand to deliver a shock to a creature you try to touch. Make a melee spell attack against the target. You have advantage on the attack roll if the target is wearing armor made of metal. On a hit, the target takes 1d8 lightning damage, and it can't take reactions until the start of its next turn. The spell's damage increases by 1d8 when you reach 5th level (2d8), 11th level (3d8), and 17th level (4d8).")
    elif(spellName == "true strike"):
        return Spell.Spell(0, "true strike", "1 action", "1 round", "30 ft", "divination", "none", "S", "foreknowledge", "You point a finger at a target in range. Your magic grants you a brief insight into the target's defenses. On your next turn, you gain advantage on your first attack roll against the target, provided that this spell hasn't ended.")

class Elf(r.Race):
    def __init__(self, age: int=100, alignment: str="chaotic good",
                 height: int=60, stats: s.Stats=s.Stats(),
                 subrace: str="high", weight: int=120,
                 gender: str="male", firstName: str="adran",
                 lastName: str="amakiir (gemflower)"):
        subrace = subrace.lower()
        wisPer = stats.getStat("wisdom: perception")
        wisPer.setHasProficiency(True)
        stats.setStat(wisPer)
        self.featuresAndTraits = ["fey ancestry: You have advantage on saving throws against being charmed, and magic can't put you to sleep",
                                  "trance: Elves do't need to sleep. Instead, they meditat deeply remaining semiconscious, for 4 hours a day. (The Common word for such meditation is 'trance.') While meditating, you can dream after a fashion; such dreams are actually mental exercises that have become reflexive through years of practice. After resting in this way, you gain the same benefit that a human does from 8 hours of sleep."]
        
        if(subrace == "dark"):
            super().__init__("elf", age, alignment, height,
                             "common elvish", "medium", stats, 30,
                             subrace, weight, gender, firstName,
                             lastName)
            self.darkvision = 120
            self.featuresAndTraits["sunlight sensitivity: You have disadvantage on attack rolls and on Wisdom (Perception) checks that rely on sight when you, the target of your attack, or whatever you are trying to perceive is in direct sunlight."]
            self.otherProficiencies = ["drow weapon training: You have proficiency with rapiers, shortswords, and hand crossbows."]
            dancingLights = Spell.Spell(0, "dancing lights",
                                        "1 action", "1 minute",
                                        "120 ft", "evocation",
                                        "none",
                                        "V, S, M (a bit of phosphourus or wychwood, or a glowworm)",
                                        "utility",
                                        "You create up to four torch-sized lights within range, making them appear as torches, lanterns, or glowing orbs that hover in the air for the duration. You can also combine the four lights into one glowing vaguely humanoid form of Medium size. Whichever form you choose, each light sheds dim light in a 10-foot radius. As a bonus action on your turn, you can move the lights up to 60 feet to a new spot within range. A light must be within 20 feet of another light created by this spell, and a light winks out if it exceeds the spell's range.")
            self.spellBook = SpellBook.SpellBook(1, 86400, 0, 0, 0,
                                                 0, 0, 0, 0, 0, 0,
                                                 [dancingLights])
            self.hasSpellBook == True
            self.spellCastingModifier = "charisma"
        elif(subrace == "wood"):
            super().__init__("elf", age, alignment, height,
                             "common elvish", "medium", stats, 35,
                             subrace, weight, gender, firstName,
                             lastName)
            self.darkvision = 60
            self.featuresAndTraits.append("mask of the wild: You can attempt to hide even when you are only lightly obscured by foliage, heavy rain, falling snow, mist, and other natural phenomena.")
            self.otherProficiencies = ["elf weapon training: You have proficiency with the longsword, shortsword, shortbow, and longbow"]
        else:
            l = r.chooseLanguage()
            super().__init__("elf", age, alignment, height,
                             "common elvish" + l, "medium", stats,
                             30, "high", weight, gender, firstName,
                             lastName)
            self.darkvision = 60
            self.otherProficiencies = ["elf weapon training: You have proficiency with the longsword, shortsword, shortbow, and longbow"]
            cantrip = chooseWizardCantrip()
            self.spellBook = SpellBook.SpellBook(1, 86400, 0, 0, 0,
                                                 0, 0, 0, 0, 0, 0,
                                                 [cantrip])
            self.hasSpellBook == True
            self.spellCastingModifier = "intelligence"


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

    def levelUp(self, level:int):
        if(self.getSubrace() == "dark"):
            if(level == 3):
                print("You now can cast faerie fire once per day")
                faerieFire = Spell.Spell(1, "faerie fire", "1 action",
                                            "1 minute",
                                            "60 ft (20 ft cube)",
                                            "evocation", "DEX save", "V",
                                            "debuff",
                                            "Each object in a 20-foot cube within range is outlined in blue, green, or violet light (your choice). Any creature in the area when the spell is cast is also outlined in light if it fails a Dexterity saving throw. For the duration, objects and affected creatures shed dim light in a 10-foot radius. Any attack roll against an affected creature or object has advantage if the attacker can see it, and the affected creature or object can't benefit from being invisible.")
                self.getSpellBook().addSpell(faerieFire)
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
                print("Nothing happens for elf at this level.")

#//----------// //----------// //----------//
# Print methods:
# These methods will print out all of the
# variables.
#//----------// //----------// //----------//
    def printRace(self, showStats: bool):
        super().printRace(showStats)
        print("Darkvision:", self.getDarkvision())
        self.printFeaturesAndTraits()
        self.printOtherProficiencies()
        if(self.getSubrace() == "high" or self.getSubrace() == "dark"):
            print("happens")
            self.spellBook.printSpellBook()

    def printFeaturesAndTraits(self):
        print("//----------// features and traits //----------//")
        for fat in self.getFeaturesAndTraits():
            print(fat)
        print("//----------// //----------// //----------//")

    def printOtherProficiencies(self):
        print("//----------// other proficiencies //----------//")
        for op in self.getOtherProficiencies():
            print(op)
        print("//----------// //----------// //----------//")


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
            print("Height not a medium creature. A elf is a medium creature between 5 ft and 6 ft, but medium creatures are between 4 ft and 8 ft")
            super().setHeight(60)

    def getOtherProficiencies(self) -> List[str]:
        return self.otherProficiencies

    def setOtherProficiencies(self, otherProficiencies: List[str]):
        self.otherProficiencies = otherProficiencies

    def getSpellBook(self) -> List[str]:
        if(self.getSubrace() == "high" or self.getSubrace() == "dark"):
            return self.spellBook
        else:
            return [""]

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





