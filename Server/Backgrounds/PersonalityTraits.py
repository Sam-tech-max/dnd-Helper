
def checkPersonalityTraits(background: str, num: str = "empty") -> str:
    background = background.lower()
    if(background == "acolyte"):
        return getPersonalityTraitAcolyte(num)
    elif(background == "charlatan"):
        return getPersonalityTraitCharlatan(num)
    elif(background == "criminal"):
        return getPersonalityTraitCriminal(num)
    elif(background == "entertainer"):
        return getPersonalityTraitEntertainer(num)
    elif(background == "folk hero"):
        return getPersonalityTraitFolkHero(num)
    else:
        return getPersonalityTraitAcolyte(num)


def getPersonalityTraitAcolyte(num:str = "empty") -> str:
    if(num == "empty" or num == "1"):
        return "I idolize a particular hero of my faith, and constantly refer to that person's deeds and example."
    elif(num == "2"):
        return "I can find common ground between the fiercest enemies, empathizing with them and always working toward peace."
    elif(num == "3"):
        return "I see omens in every event and action. The gods try to speak to us, we just need to listen."
    elif(num == "4"):
        return "Nothing can shake my optimistic attitude."
    elif(num == "5"):
        return "I quote (or misquote) sacred texts and proverbs in almost every situation"
    elif(num == "6"):
        return "I am tolerant (or intolerant) of other faiths and resqect (or condemn) the worship of other gods."
    elif(num == "7"):
        return "I've enjoyed fine food, drink, and high society among my temple's elite. Rough living grates on me."
    elif(num == "8"):
        return "I've spent so long in the temple that I have little practical experience dealing with people in the outside world."
    else:
        return num


def getPersonalityTraitCharlatan(num:str = "empty") -> str:
    if(num == "empty" or num == "1"):
        return "I fall in and out of love easily, and am always pursuing someone."
    elif(num == "2"):
        return "I have a joke for every occasion, especially occasions where humor is inappropriate."
    elif(num == "3"):
        return "Flattery is my preferred trick for getting what I want."
    elif(num == "4"):
        return "I'm born gambler who can't resist taking a risk for a potential payoff."
    elif(num == "5"):
        return "I lie about almost everything, even when there's no good reason to."
    elif(num == "6"):
        return "Sarcasm and insults are my weapons of choice."
    elif(num == "7"):
        return "I keep multiple holy symbols on me and invoke whatever deity might come in useful at any given moment."
    elif(num == "8"):
        return "I pocket anything I see that might have some value."
    else:
        return num


def getPersonalityTraitCriminal(num:str = "empty") -> str:
    if(num == "empty" or num == "1"):
        return "I always have a plan for what to do when things go wrong"
    elif(num == "2"):
        return "I am always calm, no matter what the situation. I never raise my voice or let my emotions control me."
    elif(num == "3"):
        return "The first thing I do in a new place is note the location of everything valuable - or where such things could be hidden."
    elif(num == "4"):
        return "I would rather make a new friend than a new enemy."
    elif(num == "5"):
        return "I am incredibly slow to trust. Those who seem the fairset often have the most to hide."
    elif(num == "6"):
        return "I don't pay attention to the risks in a situation. Never tell me the odds."
    elif(num == "7"):
        return "The best way to get me to do something is to tell me can't do it."
    elif(num == "8"):
        return "I blow up at the slightest insult."
    else:
        return num


def getPersonalityTraitEntertainer(num:str = "empty") -> str:
    if(num == "empty" or num == "1"):
        return "I know a story relevant to almost every situation."
    elif(num == "2"):
        return "Whenever I come to a new place, I collect local rumors and spread gossip"
    elif(num == "3"):
        return "I'm a hopeless romantic, always searching for that 'special someone.'"
    elif(num == "4"):
        return "Nobody stays angry at me or around me for long, since I can defuse any amount of tension."
    elif(num == "5"):
        return "I love a good insult, even one directed at me."
    elif(num == "6"):
        return "I get bitter if I'm not the center of attention."
    elif(num == "7"):
        return "I'll settle for nother less that perfection."
    elif(num == "8"):
        return "I change my mood or my mind as quickly as I change key in a song."
    else:
        return num


def getPersonalityTraitFolkHero(num:str = "empty") -> str:
    if(num == "empty" or num == "1"):
        return "I judge people by their actions, not their words."
    elif(num == "2"):
        return "If someone is in trouble, I'm always ready to lend help."
    elif(num == "3"):
        return "When I set my mind to something, I follow through no matter what gets in my way."
    elif(num == "4"):
        return "I have a strong sense of fair play and always try to find the most equitable solution to arguments."
    elif(num == "5"):
        return "I'm confident in my own abilities and do what I can to instill confidence in others."
    elif(num == "6"):
        return "Thinking is for other people. I prefer action."
    elif(num == "7"):
        return "I misuse long words in an attempt to sound smarter."
    elif(num == "8"):
        return "I get bored easily. When am I going to get on with my destiny?"
    else:
        return num