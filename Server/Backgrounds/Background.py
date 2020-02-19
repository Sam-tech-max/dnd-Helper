import Equipment.Item as I
import Backgrounds.Bonds as BO
import Backgrounds.Backpack as BP
import Utility.Features as FE
import Backgrounds.Flaws as FL
import Backgrounds.Ideals as ID
import Utility.Languages as LA
import Backgrounds.PersonalityTraits as PT
import Backgrounds.SkillPro as SP
import Backgrounds.ToolPro as TP
from typing import List

def checkBackgroundName(name: str) -> str:
    name = name.lower()
    if(name == "acolyte" or name == "charlatan" or
       name == "criminal" or name == "entertainer" or
       name == "folk hero" or name == "guild artisan" or
       name == "hermit" or name == "noble" or name == "outlander" or
       name == "sage" or name == "sailor" or name == "soldier" or
       name == "urchin"):
        return name
    else:
        return "acolyte"

class Background(object):
    def __init__(self, backgroundName: str = "empty",
                 backpack: List[I.Item] = [],
                 bond: str = "empty",
                 flaw: str = "empty",
                 ideal: str = "empty",
                 language: List[str] = [],
                 personalityTrait: str = "empty",
                 skillProficiencies: str = []
                 ):
        self.backgroundName = checkBackgroundName(backgroundName)
        if(len(backpack) == 0):
            self.backpack = BP.getBackpack(self.backgroundName)
        self.bond = BO.checkBond(self.backgroundName, bond)
        self.feature = FE.getBackgroundFeature(self.backgroundName)
        self.flaw = FL.checkFlaw(self.backgroundName, flaw)
        self.ideal = ID.checkIdeal(self.backgroundName, ideal)
        self.language = LA.chooseLanguageByBackground(self.backgroundName)
        self.personalityTrait = PT.checkPersonalityTraits(self.backgroundName, personalityTrait)
        if(len(skillProficiencies) == 0):
            self.skillProficiencies = SP.getSkillPro(self.backgroundName)
        else:
            self.skillProficiencies = skillProficiencies
        self.toolProficiencies = TP.getToolPro(self.backgroundName)


# //----------// //----------// //----------//
# Print Statements
# //----------// //----------// //----------//
    def printBackground(self, printSkillProficiencies: bool = False,
                        printLanguages: bool = False,
                        printBackpack: bool = False):
        print("Background: ", self.backgroundName)
        print("Bond: ", self.bond)
        print("Flaw: ", self.flaw)
        print("Ideal: ", self.ideal)
        print("Personality Trait: ", self.personalityTrait)
        print("Feature:", self.feature)
        print("Feature Discription:",
              FE.getBackgroundFeatureDiscriptionByName(str(self.feature)))
        if(printSkillProficiencies):
            self.printSkillProficiencies()
        self.printToolProficiencies()
        if(printLanguages):
            self.printLanguages()
        if(printBackpack):
            self.printBackpack()

    def printSkillProficiencies(self):
        sp = ""
        for skill in self.skillProficiencies:
            sp += ":" + skill + ":"
        print("Skill Proficiencies: ", sp)
        
    def printLanguages(self):
        l = ""
        for lang in self.language:
            l += ":" + lang + ":"
        print("Language(s): ", l)

    def printBackpack(self):
        print("//----------// Backpack //----------//")
        for item in self.backpack:
            item.printItem()

    def printToolProficiencies(self):
        tp = ""
        for pro in self.toolProficiencies:
            tp += ":" + pro + ":"
        print("Tool Proficiencies: ", tp)


# //----------// //----------// //----------//
# Main Function Statements
# //----------// //----------// //----------//
bg = Background("urchin", [], "1", "1", "1", [], "1")
bg.printBackground(False, False, False)


