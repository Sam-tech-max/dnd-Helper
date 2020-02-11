
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
    elif(background == "guild artisan"):
        return getPersonalityTraitGuildArtisan(num)
    elif(background == "hermit"):
        return getPersonalityTraitHermit(num)
    elif(background == "noble"):
        return getPersonalityTraitNoble(num)
    elif(background == "outlander"):
        return getPersonalityTraitOutlander(num)
    elif(background == "sage"):
        return getPersonalityTraitSage(num)
    elif(background == "sailor"):
        return getPersonalityTraitSailor(num)
    elif(background == "soldier"):
        return getPersonalityTraitSoldier(num)
    elif(background == "urchin"):
        return getPersonalityTraitUrchin(num)
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


def getPersonalityTraitGuildArtisan(num:str = "empty") -> str:
    if(num == "empty" or num == "1"):
        return "I believe that anything worth doing is worth doing right. I can't help it - I'm a perfectionist."
    elif(num == "2"):
        return "I'm a snob who looks down on those who can't appreciate fine art."
    elif(num == "3"):
        return "I always want to know how things work and what makes people tick."
    elif(num == "4"):
        return "I'm full of witty aphorisms and have a proverb for every occasion."
    elif(num == "5"):
        return "I'm rude to people who lack my commitment to hard work and fair play."
    elif(num == "6"):
        return "I like to talk at length about my profession."
    elif(num == "7"):
        return "I don't part with my money easily and will haggle tirelessly to get the best deal possible."
    elif(num == "8"):
        return "I'm well known for my work, and I want to make sure everyone appreciates it. I'm always taken aback when people haven't heard of me."
    else:
        return num


def getPersonalityTraitHermit(num:str = "empty") -> str:
    if(num == "empty" or num == "1"):
        return "I've been isolated for so long that I rarely speak, preferring gestures and the occasional grunt."
    elif(num == "2"):
        return "I am utterly serene, even it the face of disaster."
    elif(num == "3"):
        return "The leader of my community had something wise to say on every topic, and I am eager to share that wisdom"
    elif(num == "4"):
        return "I feel tremendous empathy for all who suffer."
    elif(num == "5"):
        return "I'm oblivious to etiquette and social expectations."
    elif(num == "6"):
        return "I connect everything that happens to me to a grand, cosmic plan."
    elif(num == "7"):
        return "I often get lost in my own thoughts and contemplation, becoming oblivious to my surroundings."
    elif(num == "8"):
        return "I am working on a grand philosophical theory and love sharing my ideas."
    else:
        return num


def getPersonalityTraitNoble(num:str = "empty") -> str:
    if(num == "empty" or num == "1"):
        return "My eloquent flattery makes everyone I talk to feel like the most wonderful and important person in the world."
    elif(num == "2"):
        return "The common folk love me for my kindness and generosity."
    elif(num == "3"):
        return "No one could doubt by looking at my regal bearing that I am a cut above the unwashed masses."
    elif(num == "4"):
        return "I take great pains to always look my best and follow the latest fashions."
    elif(num == "5"):
        return "I don't like to get my hands dirty, and I won't be caught dead in unsuitable accommodations."
    elif(num == "6"):
        return "despite my noble birth, I do not place myself above other folk. We all have the same blood."
    elif(num == "7"):
        return "My favor, once lost, is lost forever."
    elif(num == "8"):
        return "If you do me an injury, I will crush you, ruin your name, and salt your fields."
    else:
        return num


def getPersonalityTraitOutlander(num:str = "empty") -> str:
    if(num == "empty" or num == "1"):
        return "I'm driven by a wanderlust that led me away from home."
    elif(num == "2"):
        return "I watch over my friends as if they were a litter of newborn pups."
    elif(num == "3"):
        return "I once ran twenty-five miles without stopping to warn my clan of an approaching orc horde. I'd do it again if I had to."
    elif(num == "4"):
        return "I have a lesson for every situation, drawn from observing nature."
    elif(num == "5"):
        return "I place no stock in wealthy or well-mannered folk. Money and manners won't save you from a hungry owlbear."
    elif(num == "6"):
        return "I'm always picking things up, absently fiddling with them, and sometimes accidentally breaking them."
    elif(num == "7"):
        return "I feel far more comfortable around animals than people."
    elif(num == "8"):
        return "I was, in fact, raised by wolves."
    else:
        return num


def getPersonalityTraitSage(num:str = "empty") -> str:
    if(num == "empty" or num == "1"):
        return "I use polysyliabic words that convey the impression of great erudition."
    elif(num == "2"):
        return "I've read every book in the world's greatest libraries - or I like to boast that I have."
    elif(num == "3"):
        return "I'm used to helping out those who aren't as smart as I am, and I patiently explain anything and everything to others."
    elif(num == "4"):
        return "There's nothing I like more than a good mystery."
    elif(num == "5"):
        return "I'm willing to listen to every side of an argument before I make my own judgment."
    elif(num == "6"):
        return "I...speak...slowly...when talking...to idiots,...which...almost...everyone...is...compared...to me."
    elif(num == "7"):
        return "I am horribly, horribly awkward in social situations."
    elif(num == "8"):
        return "I'm convinced that people are always trying to steal my secrets."
    else:
        return num


def getPersonalityTraitSailor(num:str = "empty") -> str:
    if(num == "empty" or num == "1"):
        return "My friends know they can rely on me, no matter what."
    elif(num == "2"):
        return "I work hard so that I can play hard when the work is done."
    elif(num == "3"):
        return "I enjoy sailing into new ports and making new friends over a flagon of ale."
    elif(num == "4"):
        return "I stretch the truth for the sake of a good story."
    elif(num == "5"):
        return "To me, a tavern brawl is a nice way to get to know a new city."
    elif(num == "6"):
        return "I never pass up a friendly wager."
    elif(num == "7"):
        return "My language is as foul as an otyugh nest."
    elif(num == "8"):
        return "I like a job well done, especially if I can convice someone else to do it."
    else:
        return num


def getPersonalityTraitSoldier(num:str = "empty") -> str:
    if(num == "empty" or num == "1"):
        return "I'm always polite and respectful."
    elif(num == "2"):
        return "I'm haunted by memories of war. I can't get the images of violence out of my mind."
    elif(num == "3"):
        return "I've lost too many friends, and I'm slow to make new ones."
    elif(num == "4"):
        return "I'm full of inspiring and cautionary tales from my military experience relevant to almost every combat situation."
    elif(num == "5"):
        return "I can stare down a hell bound without flinching."
    elif(num == "6"):
        return "I enjoy being strong and like breaking things."
    elif(num == "7"):
        return "I have a crude sense of humor."
    elif(num == "8"):
        return "I face problems head-on. A simple, direct solution is the best path to success."
    else:
        return num


def getPersonalityTraitUrchin(num:str = "empty") -> str:
    if(num == "empty" or num == "1"):
        return "I hide scraps of food and trinkets away in my pockets."
    elif(num == "2"):
        return "I ask a lot of questions."
    elif(num == "3"):
        return "I like to squeeze into small places where no one else can get to me."
    elif(num == "4"):
        return "I sleep with my back to a wall or tree, with everything I own wrapped in a bundle in my arms."
    elif(num == "5"):
        return "I eat like a pig and have bad manners."
    elif(num == "6"):
        return "I think anyone who's nice to me is hiding evil intent."
    elif(num == "7"):
        return "I don't like to bathe."
    elif(num == "8"):
        return "I bluntly say what other people are hinting at or hiding."
    else:
        return num
