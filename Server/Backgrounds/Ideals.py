
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
    elif(background == "guild artisan"):
        return getIdealGuildArtisan(num)
    elif(background == "hermit"):
        return getIdealHermit(num)
    elif(background == "noble"):
        return getIdealNoble(num)
    elif(background == "outlander"):
        return getIdealOutlander(num)
    elif(background == "sage"):
        return getIdealSage(num)
    elif(background == "sailor"):
        return getIdealSailor(num)
    elif(background == "soldier"):
        return getIdealSoldier(num)
    elif(background == "urchin"):
        return getIdealUrchin(num)
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


def getIdealGuildArtisan(num:str = "empty") -> str:
    if(num == "empty" or num == "1"):
        return "Community. It is the duty of all civilized people to strengthen the bonds of community and the security of civilization. (Lawful)"
    elif(num == "2"):
        return "Generosity. My talents were given to me so that I could use them to benefit the world. (Good)"
    elif(num == "3"):
        return "Freedom. Everyone should be free to pursue his or her own livelihood. (Chaotic)"
    elif(num == "4"):
        return "Greed. I'm only in it for the money. (Evil)"
    elif(num == "5"):
        return "People. I'm committed to the people I care about, not to ideals. (Neutral)"
    elif(num == "6"):
        return "Aspiration. I work hard to be the best there is at my craft."
    else:
        return num


def getIdealHermit(num:str = "empty") -> str:
    if(num == "empty" or num == "1"):
        return "Greater Good. My gifts are meant to be shared with all, not used for my own benefit. (Good)"
    elif(num == "2"):
        return "Logic. Emotions must not cloud our sense of what is right and true, or our logical thinking. (Lawful)"
    elif(num == "3"):
        return "Free Thinking. Inquiry and curiosity are the pillars of progress. (Chaotic)"
    elif(num == "4"):
        return "Power. Solitude and contemplation are paths toward mystical or magical power. (Evil)"
    elif(num == "5"):
        return "Live and Let Live. Meddling in the affaris of others only causes trouble. (Neutral)"
    elif(num == "6"):
        return "Self-Knowledge. If you know yourself, there's nothing left to know. (Any)"
    else:
        return num


def getIdealNoble(num:str = "empty") -> str:
    if(num == "empty" or num == "1"):
        return "Respect. Respect is due to me because of my position, but all people regardless of statiion deserve to be treated with dignity. (Good)"
    elif(num == "2"):
        return "Responsibility. It is my buty to respect the authority of those above me, just as those below me must respect mine. (Lawful)"
    elif(num == "3"):
        return "Independence. I must prove that I can handle myself without the coddling of my family. (Chaotic)"
    elif(num == "4"):
        return "Power. If I can attain more power, no one will tell me what to do. (Evil)"
    elif(num == "5"):
        return "Family. Blood runs thicker than water. (Any)"
    elif(num == "6"):
        return "Noble Obligation. It is my duty to protect and car for the people beneath me. (Good)"
    else:
        return num


def getIdealOutlander(num:str = "empty") -> str:
    if(num == "empty" or num == "1"):
        return "Change. Life is like the seasons, in constant change, and we must change with it. (Chaotic)"
    elif(num == "2"):
        return "Greater Good. It is each person's responsibility to make the most happiness for the whole tribe. (Good)"
    elif(num == "3"):
        return "Honor. If I dishonor myself, I dishonor my whole clan. (Lawful)"
    elif(num == "4"):
        return "Might. The strongest are meant to rule. (Evil)"
    elif(num == "5"):
        return "Nature. The natural world is more important than all the constructs of civilization. (Neutral)"
    elif(num == "6"):
        return "Glory. I must earn glory in battle, for myself and my clan. (Any)"
    else:
        return num


def getIdealSage(num:str = "empty") -> str:
    if(num == "empty" or num == "1"):
        return "Knowledge. The path to power and self-improvement is through knowledge. (Neutral)"
    elif(num == "2"):
        return "Beauty. What is beautiful points us beyond itself toward what is true. (Good)"
    elif(num == "3"):
        return "Logic. Emotions must not cloud our logical thinking. (Lawful)"
    elif(num == "4"):
        return "No Limits. Nothing should fetter the infinite possibility inherent in all existence. (Chaotic)"
    elif(num == "5"):
        return "Power. Knowledge is the path to power and domination. (Evil)"
    elif(num == "6"):
        return "Self-Improvement. The goal of a life of study is the betterment of oneself. (Any)"
    else:
        return num


def getIdealSailor(num:str = "empty") -> str:
    if(num == "empty" or num == "1"):
        return "Respect. The thing that keeps a ship together is mutual respect between captin and crew. (Good)"
    elif(num == "2"):
        return "Rairness. We all do the work, so we all share in the rewards. (Lawful)"
    elif(num == "3"):
        return "Freedom. The sea is freedom - the freedom to go anywhere and do anything. (Chaotic)"
    elif(num == "4"):
        return "Mastery. I'm a predator, and the other ships on the sea are my prey. (Evil)"
    elif(num == "5"):
        return "People. I'm committed to my crewmates, not to ideals. (Neutral)"
    elif(num == "6"):
        return "Aspiration. Someday I'll own my own ship and chart my own destiny. (Any)"
    else:
        return num


def getIdealSoldier(num:str = "empty") -> str:
    if(num == "empty" or num == "1"):
        return "Greater Good. Our lot is to lay down our lives in defense of others. (Good)"
    elif(num == "2"):
        return "Responsibility. I do what I must and obey just authority. (Lawful)"
    elif(num == "3"):
        return "Independence. When people follow orders blindly, they embrace a kind of tyranny. (Chaotic)"
    elif(num == "4"):
        return "Might. In life as in war, the stronger force wins. (Evil)"
    elif(num == "5"):
        return "Live and Let Live. Ideals aren't worth killing over or going to war for. (Neutral)"
    elif(num == "6"):
        return "Nation. My city, nation, or people are all that matter. (Any)"
    else:
        return num


def getIdealUrchin(num:str = "empty") -> str:
    if(num == "empty" or num == "1"):
        return "Respect. All people, rich or poor, deserve respect. (Good)"
    elif(num == "2"):
        return "Community. We have to take care of each other, beacuse no one else is going to do it. (Lawful)"
    elif(num == "3"):
        return "Change. The low are lifted up, and the high and mighty are brought down. Change is the nature of things. (Chaotic)"
    elif(num == "4"):
        return "Retribution. The rich need to be shown what life and death are like in the gutters. (Evil)"
    elif(num == "5"):
        return "People. I help the people who help me - that's what keeps us alive. (Neutral)"
    elif(num == "6"):
        return "Aspiration. I'm going to prove that I'm worthy of a better life."
    else:
        return num
