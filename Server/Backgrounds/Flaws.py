

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
    elif(background == "guild artisan"):
        return getFlawGuildArtisan(num)
    elif(background == "hermit"):
        return getFlawHermit(num)
    elif(background == "noble"):
        return getFlawNoble(num)
    elif(background == "outlander"):
        return getFlawOutlander(num)
    elif(background == "sage"):
        return getFlawSage(num)
    elif(background == "sailor"):
        return getFlawSailor(num)
    elif(background == "soldier"):
        return getFlawSoldier(num)
    elif(background == "urchin"):
        return getFlawUrchin(num)
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


def getFlawGuildArtisan(num:str = "empty") -> str:
    if(num == "empty" or num == "1"):
        return "I'll do anything to get my hands on something rare or priceless."
    elif(num == "2"):
        return "I'm quick to assume that someone is trying to cheat me."
    elif(num == "3"):
        return "No one must ever learn that I once stole money from guild coffers."
    elif(num == "4"):
        return "I'm never satisfied with what I have - I always want more."
    elif(num == "5"):
        return "I would kill to acquire a noble title."
    elif(num == "6"):
        return "I'm horribly jealous of anyone who can outshine my handiwork. Everywhere I go. I'm surronded by rivals."
    else:
        return num
    

def getFlawHermit(num:str = "empty") -> str:
    if(num == "empty" or num == "1"):
        return "Now that I've returned to the world, I enjoy its delights a little too much."
    elif(num == "2"):
        return "I harbor dark, bloodthirsty thoughts that my isolation and meditation failed to quell."
    elif(num == "3"):
        return "I am dogmatic in my thoughts and philosophy."
    elif(num == "4"):
        return "I let my need to win arguments overshadow frendships and harmony."
    elif(num == "5"):
        return "I'd risk too much to uncover a lost bit of knowledge."
    elif(num == "6"):
        return "I like keeping secrets and won't share them with anyone."
    else:
        return num


def getFlawNoble(num:str = "empty") -> str:
    if(num == "empty" or num == "1"):
        return "I secretly believe that everyone is beneath me."
    elif(num == "2"):
        return "I hide a truly scandalous secret that could ruin my family forever."
    elif(num == "3"):
        return "I too often hear veiled insults and threats in every word addressed to me, and I'm quick to anger."
    elif(num == "4"):
        return "I have an insatiable desire for carnal pleasures."
    elif(num == "5"):
        return "In fact, the world does revolve around me."
    elif(num == "6"):
        return "By my words and actions, I often bring shame to my family."
    else:
        return num


def getFlawOutlander(num:str = "empty") -> str:
    if(num == "empty" or num == "1"):
        return "I am too enamored of ale, wine, and other intoxicants."
    elif(num == "2"):
        return "There's no room for caution in a life lived to the fullest."
    elif(num == "3"):
        return "I remember every insult I've received and nurse a silent resentment toward anyone who's ever wronged me."
    elif(num == "4"):
        return "I am slow to trust members of other races, tribes, and societies."
    elif(num == "5"):
        return "Violence is my answer to almost any challenge."
    elif(num == "6"):
        return "Don't expect me to save those who can't save themselves. It is nature's way that the strong thrive and the weak perish."
    else:
        return num


def getFlawSage(num:str = "empty") -> str:
    if(num == "empty" or num == "1"):
        return "I am easily distracted by the promise of information."
    elif(num == "2"):
        return "Most people scream and run when they see a demon. I stop and take notes on its anatomy."
    elif(num == "3"):
        return "Unlocking an ancient mystery is worth the price of a civilization."
    elif(num == "4"):
        return "I overlook obvious solutions in favor of complicated ones."
    elif(num == "5"):
        return "I speak without really thinking through my words, invariably insulting others."
    elif(num == "6"):
        return "I can't keep a secret to save my life, or anyone else's."
    else:
        return num


def getFlawSailor(num:str = "empty") -> str:
    if(num == "empty" or num == "1"):
        return "I follow orders, even if I think they're wrong"
    elif(num == "2"):
        return "I'll say anything to avoid having to do extra work."
    elif(num == "3"):
        return "Once someone questions my courage, I never back down no matter how dangerous the situation."
    elif(num == "4"):
        return "Once I start drinking, it's hard for me to stop."
    elif(num == "5"):
        return "I can't help but pocket loose coins and other trinkets I come across."
    elif(num == "6"):
        return "My pride will probably lead to my destruction."
    else:
        return num


def getFlawSoldier(num:str = "empty") -> str:
    if(num == "empty" or num == "1"):
        return "The monstrous enemy we faced in battle still leaves me quivering with fear."
    elif(num == "2"):
        return "I have little respect for anyone who is not a proven warrior."
    elif(num == "3"):
        return "I made a terrible mistake in battle cost many lives - and I would do anything to keep that mistake secret."
    elif(num == "4"):
        return "My hatred of my enemies is blind and unreasoning."
    elif(num == "5"):
        return "I obey the law, even if the law causes misery."
    elif(num == "6"):
        return "I'd rather eat my armor than admit when I'm wrong."
    else:
        return num


def getFlawUrchin(num:str = "empty") -> str:
    if(num == "empty" or num == "1"):
        return "If I'm outnumbered, I will run away from a fight."
    elif(num == "2"):
        return "Gold seems like a lot of money to me, and I'll do just about anything for more of it."
    elif(num == "3"):
        return "I will never fully trust anyone other than myself."
    elif(num == "4"):
        return "I'd rather kill someone in their sleep then fight fair."
    elif(num == "5"):
        return "It's not stealing if I need it more than someone else."
    elif(num == "6"):
        return "People who can't take care of themselves get what they deserve."
    else:
        return num
