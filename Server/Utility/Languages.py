from typing import List

def isLanguage(l: str = "empty") -> bool:
    l = l.lower()
    if (l == "abyssal" or l == "aquan" or l == "auran" or
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

def chooseLanguage(l: str = "empty")->str:
    l = l.lower()
    if (isLanguage(l)):
        return l
    else:
        print("Please choose from the following languages:")
        l = str(input("abyssal, aquan, auran, celestial, common, deep, draconic, druidic, dwarvish elvish, giant, gnomish, goblin, gnoll, halfling, ignan, infernal, orc, primordial, sylvan, terran, or undercommon: "))
        return chooseLanguage(l)

def chooseLanguageByBackground(background: str) -> List[str]:
    background = background.lower()
    if(background == "acolyte" or background == "sage"):
        lang1 = chooseLanguage()
        lang2 = chooseLanguage()
        return [lang1, lang2]
    elif(background == "guild artisan" or background == "hermit" or
         background == "noble" or background == "outlander"):
        lang1 = chooseLanguage()
        return [lang1]
    return []
