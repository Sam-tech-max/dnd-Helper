
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
    elif(background == "guild artisan"):
        return getBondGuildArtisan(num)
    elif(background == "hermit"):
        return getBondHermit(num)
    elif(background == "noble"):
        return getBondNoble(num)
    elif(background == "outlander"):
        return getBondOutlander(num)
    elif(background == "sage"):
        return getBondSage(num)
    elif(background == "sailor"):
        return getBondSailor(num)
    elif(background == "soldier"):
        return getBondSoldier(num)
    elif(background == "urchin"):
        return getBondUrchin(num)
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


def getBondGuildArtisan(num:str = "empty") -> str:
    if(num == "empty" or num == "1"):
        return "The workshop where I learned my trade is the most important place in the world to me."
    elif(num == "2"):
        return "I created a great work for someone, and then found them unworthy to receive it. I'm still looking for someone worthy."
    elif(num == "3"):
        return "I owe my guild a great debt for forging me into the person I am today."
    elif(num == "4"):
        return "I pursue wealth to secure someone's love."
    elif(num == "5"):
        return "One day I will return to my guild and prove that I am the greatest artisan of them all."
    elif(num == "6"):
        return "I will get revenge on the evil forces that destroyed my place of business and ruined my livelihood."
    else:
        return num


def getBondHermit(num:str = "empty") -> str:
    if(num == "empty" or num == "1"):
        return "Nothing is more important than the other members of my hermitage, other, or association."
    elif(num == "2"):
        return "I entered seclusion to hide from the ones who might still be hunting me. I must someday confront them."
    elif(num == "3"):
        return "I'm still seeking the enlightenment I pursued in my seclusion, and it still eludes me."
    elif(num == "4"):
        return "I entered seclusion because I loved someone I could not have."
    elif(num == "5"):
        return "Should my discovery come to light, it could bring ruin to the world."
    elif(num == "6"):
        return "My isolation gave me great insight into a great evil that only I can destroy."
    else:
        return num


def getBondNoble(num:str = "empty") -> str:
    if(num == "empty" or num == "1"):
        return "I will face any challenge to win the approval of my family."
    elif(num == "2"):
        return "My house's alliance with another noble family must be sustained at all costs."
    elif(num == "3"):
        return "Nothing is more important than the other members of my family."
    elif(num == "4"):
        return "I am in love with the heir of a family that my family despises."
    elif(num == "5"):
        return "My loyalty to my sovereign is unwavering."
    elif(num == "6"):
        return "The common folk must see me as a hero of the people."
    else:
        return num


def getBondOutlander(num:str = "empty") -> str:
    if(num == "empty" or num == "1"):
        return "My family, clan, or tribe is the most important thing in my life, even when they are far from me."
    elif(num == "2"):
        return "An injury to the unspoiled wilderness of my home is an injury to me."
    elif(num == "3"):
        return "I will bring terrible wrath down on the evildoers who destroyed my homeland."
    elif(num == "4"):
        return "I am the last of my tribe, and it is up to me to ensure their names enter legend."
    elif(num == "5"):
        return "I suffer awlful visions of a coming disaster and will do anything to prevent it."
    elif(num == "6"):
        return "It is my duty to provide children to sustain my tribe."
    else:
        return num


def getBondSage(num:str = "empty") -> str:
    if(num == "empty" or num == "1"):
        return "It is my duty to protect my students."
    elif(num == "2"):
        return "I have an ancient text that holds terrible secrets that must not fall into the wrong hands."
    elif(num == "3"):
        return "I work to preserve a library, university, sciptorium, or monastery."
    elif(num == "4"):
        return "My life's work is a series of tomes related to a specific field of lore."
    elif(num == "5"):
        return "I've been searching my whole life for the answer to a certain question."
    elif(num == "6"):
        return "I sold my soul for knowledge. I hope to do great deeds and win it back."
    else:
        return num


def getBondSailor(num:str = "empty") -> str:
    if(num == "empty" or num == "1"):
        return "I'm loyal to my captain first, everything else second."
    elif(num == "2"):
        return "The ship is most important - crewmates and captains come and go."
    elif(num == "3"):
        return "I'll always remember my first ship."
    elif(num == "4"):
        return "In a harbor town, I have a paramour whose eyes nearly stole me from the sea."
    elif(num == "5"):
        return "I was cheated out of my fair share of the profits, and I want to get my due."
    elif(num == "6"):
        return "Ruthless pirates murdered my captain and crewmates, plundered our ship, and left me to die. Vengeance will be mine."
    else:
        return num


def getBondSoldier(num:str = "empty") -> str:
    if(num == "empty" or num == "1"):
        return "I would still lay down my life for the people I served with."
    elif(num == "2"):
        return "Someone saved my life on the battlefield. To this day, I will never leave a friend behind."
    elif(num == "3"):
        return "My honor is my life."
    elif(num == "4"):
        return "I'll never forget the crushing defeat my company suffered or the enemies who dealt it."
    elif(num == "5"):
        return "Those who fight beside me are those worth dying for."
    elif(num == "6"):
        return "I fight for those who cannot fight for themselves."
    else:
        return num


def getBondUrchin(num:str = "empty") -> str:
    if(num == "empty" or num == "1"):
        return "My town or city is my home, and I'll fight to defend it."
    elif(num == "2"):
        return "I sponsor an orphanage to keep others from enduring what I was forced to endure."
    elif(num == "3"):
        return "I owe my survival to another urchin who taught me to live on the streets."
    elif(num == "4"):
        return "I owe a debt I can never repay to the person who took pity on me."
    elif(num == "5"):
        return "I escaped my life of poverty by robbing an important person, and I'm wanted for it."
    elif(num == "6"):
        return "No one else should have to endure the hardships I've been through."
    else:
        return num
