
def checkIdeal(background: str, num: str = "empty") -> str:
    background = background.lower()
    if(background == "acolyte"):
        return getIdealAcolyte(num)
    elif(background == "charlatan"):
        return getIdealCharlatan(num)
    elif(background == "criminal"):
        return getIdealCriminal(num)
    elif(background == "entertainer"):
        return getIdealEntertainer(num)
    elif(background == "folk hero"):
        return getIdealFolkHero(num)
    else:
        return getIdealAcolyte(num)


def getIdealAcolyte(num:str = "empty") -> str:
    if(num == "empty" or num == "1"):
        return "Tradition. The ancient traditions of worship and sacrifice must be preserved and upheld. (Lawful)"
    elif(num == "2"):
        return "Charity. I always try to help those in need, no matter what the personal cost. (Good)"
    elif(num == "3"):
        return "Change. We must help bring about the changes the gods are constantly working in the world. (Chaotic)"
    elif(num == "4"):
        return "Power. I hope to one day rise to the top of my faith's religious hierarchy. (Lawful)"
    elif(num == "5"):
        return "Faith. I trush that my deity will guide my actions. I have faith that if I work hard, things with go well. (Lawful)"
    elif(num == "6"):
        return "Aspiration. I seek to prove myself workthy of my god's favor by matching my action against his or her teachings. (Any)"
    else:
        return num


def getIdealCharlatan(num:str = "empty") -> str:
    if(num == "empty" or num == "1"):
        return "Independence. I am a free spireit - no one tells me what to do. (Chaotic)"
    elif(num == "2"):
        return "Fairness. I never target people who can't afford to lose a few coins. (Lawful)"
    elif(num == "3"):
        return "Charity. I distribute the money I acquire to the people who really need it. (Good)"
    elif(num == "4"):
        return "Creativity. I never run the same con twice. (Chaotic)"
    elif(num == "5"):
        return "Friendship. Material goods come and go. Bonds of friendship last forever. (Good)"
    elif(num == "6"):
        return "Aspiration. I'm determined to make something of myself. (Any)"
    else:
        return num


def getIdealCriminal(num:str = "empty") -> str:
    if(num == "empty" or num == "1"):
        return "Honor. I don't steal from others in the trade. (Lawful)"
    elif(num == "2"):
        return "Freedom. Chains are meant to be broken, as are those who would forge them. (Chaotic)"
    elif(num == "3"):
        return "Charity. I steal from the wealthy so that I can help people in need. (Good)"
    elif(num == "4"):
        return "Greed. I will do whatever it takes to become wealthy. (Evil)"
    elif(num == "5"):
        return "People. I'm loyal to my friends, not to any ideals, and everyone else can take a trip down the Styx for all I care. (Neutral)"
    elif(num == "6"):
        return "Redemption. There's a spark of good in everyone. (Good)"
    else:
        return num


def getIdealEntertainer(num:str = "empty") -> str:
    if(num == "empty" or num == "1"):
        return "Beauty. When I perform, I make the world better than it was. (Good)"
    elif(num == "2"):
        return "Tradition. The stories, legends, and songs of the past must never be forgotten, for they teach us who we are. (Lawful)"
    elif(num == "3"):
        return "Creativity. The world is in need of new ideas and bold action. (Chaotic)"
    elif(num == "4"):
        return "Greed. I'm only in it for the money and fame. (Evil)"
    elif(num == "5"):
        return "People. I like seeing the smiles on people's faces when I perform. That's all that matters. (Neutral)"
    elif(num == "6"):
        return "Honesty. Art should reflect the sould; it should come from within and reveal who we really are. (Any)"
    else:
        return num


def getIdealFolkHero(num:str = "empty") -> str:
    if(num == "empty" or num == "1"):
        return "Respect. People deserve to be treated with dignity and respect. (Good)"
    elif(num == "2"):
        return "Fairness. No one should get preferential treatment before the law, and no one is above the law. (Lawful)"
    elif(num == "3"):
        return "Freedom. Tyrants must nont be allowed to oppress the people. (Chaotic)"
    elif(num == "4"):
        return "Might. If I become strong, I can take what I want - what I deserve. (Evil)"
    elif(num == "5"):
        return "Sincerity. There's no good in pretending to be something I'm not. (Neutral)"
    elif(num == "6"):
        return "Destiny. Nothing and no one can steer me away from my higher calling. (Any)"
    else:
        return num