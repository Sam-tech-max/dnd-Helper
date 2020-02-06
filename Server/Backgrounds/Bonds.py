
def checkBond(background: str, num: str = "empty") -> str:
    background = background.lower()
    if(background == "acolyte"):
        return getBondAcolyte(num)
    elif(background == "charlatan"):
        return getBondCharlatan(num)
    elif(background == "criminal"):
        return getBondCriminal(num)
    elif(background == "entertainer"):
        return getBondEntertainer(num)
    elif(background == "folk hero"):
        return getBondFolkHero(num)
    else:
        return getBondAcolyte(num)


def getBondAcolyte(num:str = "empty") -> str:
    if(num == "empty" or num == "1"):
        return "I would die to recover an ancient relic of my faith that was lost long ago."
    elif(num == "2"):
        return "I will someday get revenge on the corrupt temple hierarchy who branded me a heretic"
    elif(num == "3"):
        return "I owe my life to the priest who took me in when my parents died."
    elif(num == "4"):
        return "Everything I do is for the common people"
    elif(num == "5"):
        return "I will do anything to protect the temple where I served."
    elif(num == "6"):
        return "I seek to preserve a sacred text that my enemies consider heretical and seek to destroy."
    else:
        return num

def getBondCharlatan(num:str = "empty") -> str:
    if(num == "empty" or num == "1"):
        return "I fleeced the wrong person and must work to ensure that this individual never crosses paths with me or those I care about"
    elif(num == "2"):
        return "I owe everything to my mentor - a horrible person who's probably rotting in jail somewhere"
    elif(num == "3"):
        return "Somewhere out there, I have a child who doesn't know me. I'm making the world better for him or her."
    elif(num == "4"):
        return "I come from a noble family, and one day I'll reclaim my lands and title from those who stole them from me."
    elif(num == "5"):
        return "A powerful person killed someone I love. Some day soon, I'll have my revenge."
    elif(num == "6"):
        return "I swindled and ruined a person who didn't deserve it. I seek to atone for my misdees but might never be able to forgive myself."
    else:
        return num


def getBondCriminal(num:str = "empty") -> str:
    if(num == "empty" or num == "1"):
        return "I'm trying to pay off an old debt I owe to a generous benefactor."
    elif(num == "2"):
        return "My ill-gotten gains go to support my family."
    elif(num == "3"):
        return "Something important was taken from me, and I aim to steal it back."
    elif(num == "4"):
        return "I will become the greatest thief that ever lived."
    elif(num == "5"):
        return "I'm guilty of a terrible crime. I hope I can redeem myself for it."
    elif(num == "6"):
        return "Someone I loved died because of 1 mistake I made. That will never happen again"
    else:
        return num


def getBondEntertainer(num:str = "empty") -> str:
    if(num == "empty" or num == "1"):
        return "My instrument is my most treasured possession, and it remunds me of someone I love."
    elif(num == "2"):
        return "Someone stole my precious instrument, and someday I'll get in back."
    elif(num == "3"):
        return "I want to be famous, whatever it takes."
    elif(num == "4"):
        return "I idolize a hero of the old tales and measure my deeds against that person's."
    elif(num == "5"):
        return "I will do anything to prove myself superior to my hated rival."
    elif(num == "6"):
        return "I would do anything for the other members of my old troupe."
    else:
        return num


def getBondFolkHero(num:str = "empty") -> str:
    if(num == "empty" or num == "1"):
        return "I have a family, but I have no idea where they are. One day, I hope to see them again."
    elif(num == "2"):
        return "I worked the land, I love the land, and I will protect the land."
    elif(num == "3"):
        return "A proud noble once gave me a horrible beating, and I will take my revenge on any bully I encounter."
    elif(num == "4"):
        return "My tools are symbols of my past life, and I carry them so that I will never forget my roots."
    elif(num == "5"):
        return "I protect those who cannot protect themselves."
    elif(num == "6"):
        return "I wish my childhood sweetheart had come with me to pursue my destiny."
    else:
        return num
