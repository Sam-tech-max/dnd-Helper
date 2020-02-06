

def checkFlaw(background: str, num: str = "empty") -> str:
    background = background.lower()
    if(background == "acolyte"):
        return getFlawAcolyte(num)
    elif(background == "charlatan"):
        return getFlawCharlatan(num)
    elif(background == "criminal"):
        return getFlawCriminal(num)
    elif(background == "entertainer"):
        return getFlawEntertainer(num)
    elif(background == "folk hero"):
        return getFlawFolkHero(num)
    else:
        return getFlawAcolyte(num)


def getFlawAcolyte(num:str = "empty") -> str:
    if(num == "empty" or num == "1"):
        return "I judge others harshly, and myself even more severely."
    elif(num == "2"):
        return "I put too much trust in those who wield power within my temple's hierarchy."
    elif(num == "3"):
        return "My piety sometimes leads me to blindly trust those that profess faith in my god."
    elif(num == "4"):
        return "I am inflexible in my thinking."
    elif(num == "5"):
        return "I am suspicious of strangers and expect the worst of them."
    elif(num == "6"):
        return "Once I pick a goal, I become obsessed with it to the detriment of everything else in my life."
    else:
        return num


def getFlawCharlatan(num:str = "empty") -> str:
    if(num == "empty" or num == "1"):
        return "I can't resist a pretty face."
    elif(num == "2"):
        return "I'm always in debt. I spend my ill-gotten gains on decadent luxuries faster that I bring them in."
    elif(num == "3"):
        return "I'm convinced that no one could ever fool me the way I fool others."
    elif(num == "4"):
        return "I'm too greedy for my own good. I can't resist taking a risk if there's money involved."
    elif(num == "5"):
        return "I can't resist swindling people who are more powerful than me."
    elif(num == "6"):
        return "I hate to admit it and will hate myself for it, but I'll run and preserved my own hide if the going gets tough."
    else:
        return num


def getFlawCriminal(num:str = "empty") -> str:
    if(num == "empty" or num == "1"):
        return "When I see something valuable, I can't think about anything but how to steal it."
    elif(num == "2"):
        return "When faced with a choice between money and my friends, I usually choose the money."
    elif(num == "3"):
        return "If there's a plan, I'll forget it. If I don't forget it, I'll ignore it."
    elif(num == "4"):
        return "I have a 'tell' that reveals when I'm lying."
    elif(num == "5"):
        return "I turn tail and run when things look bad."
    elif(num == "6"):
        return "An innocent person is in prison for a crime that I committed. I'm oday with that."
    else:
        return num


def getFlawEntertainer(num:str = "empty") -> str:
    if(num == "empty" or num == "1"):
        return "I'll do anything to win fame and renown"
    elif(num == "2"):
        return "I'm a sucker for a pretty face."
    elif(num == "3"):
        return "A scandal prevents me from ever going home again. That kind of trouble seems to follow me around."
    elif(num == "4"):
        return "I once satirized a noble who still wants my head. It was a mistake that I will likely repeat."
    elif(num == "5"):
        return "I have trouble keeping my true feelings hidden. My sharp tongue lands me in trouble."
    elif(num == "6"):
        return "Despite my best efforts, I am unreliable to my friends."
    else:
        return num


def getFlawFolkHero(num:str = "empty") -> str:
    if(num == "empty" or num == "1"):
        return "The tyrant who rules my land will stop at nothing to see me killed."
    elif(num == "2"):
        return "I'm convinced of the significance of my destiny, and blind to my shortcomings and the fisk of failure"
    elif(num == "3"):
        return "The people who knew me when I was young know my shameful secret, so I can never go home again."
    elif(num == "4"):
        return "I have a weakness for the vices of the city, especially hard drink."
    elif(num == "5"):
        return "Secretly, I believe that things would be better if I were a tyrant lording over the land."
    elif(num == "6"):
        return "I have trouble trusting in my allies."
    else:
        return num