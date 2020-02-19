


def getBackgroundFeature(background: str) -> str:
    background = background.lower()
    if(background == "acolyte"):
        return "shelter of the faithful"
    elif(background == "charlatan"):
        return "false identity"
    elif(background == "criminal"):
        return "criminal contact"
    elif(background == "entertainer"):
        return "by popular demand"
    elif(background == "folk hero"):
        return "rustic hospitality"
    elif(background == "guild artisan"):
        return "guild membership"
    elif(background == "hermit"):
        return "discovery"
    elif(background == "noble"):
        return "position of privilege"
    elif(background == "outlander"):
        return "wanderer"
    elif(background == "sage"):
        return "researcher"
    elif(background == "sailor"):
        return "ship's passage"
    elif(background == "soldier"):
        return "military rank"
    elif(background == "urchin"):
        return "city secrets"


def getBackgroundFeatureDiscriptionByName(feature: str) -> str:
    feature = feature.lower()
    if(feature == "by popular demand"):
        return byPopularDemandDiscription()
    elif(feature == "city secrets"):
        return citySecretsDiscription()
    elif(feature == "criminal contact"):
        return criminalContactDiscription()
    elif(feature == "discovery"):
        return discoveryDiscription()
    elif(feature == "false identity"):
        return falseIdentityDiscription()
    elif(feature == "guild membership"):
        return guildMembershipDiscription()
    elif(feature == "military rank"):
        return militaryRankDiscription()
    elif(feature == "position of privilege"):
        return positionOfPrivilegeDiscription()
    elif(feature == "rustic hospitality"):
        return rusticHospitalityDiscription()
    elif(feature == "researcher"):
        return researcherDiscription()
    elif(feature == "shelter of the faithful"):
        return shelterOfTheFaithfulDiscription()
    elif(feature == "ship's passage"):
        return shipsPassageDiscription()
    elif(feature == "wanderer"):
        return wandererDiscription()


def byPopularDemandDiscription() -> str:
    d = "You can always find a place to perform , usually in an inn "
    d += "or tavern but possibly with a circus, at a theater, or eve"
    d += "n in a noble�s court. At such a place, you receive free lo"
    d += "dging and food of a modest or comfortable standard (depend"
    d += "ing on the quality of the establishment), as long as you p"
    d += "erform each night. In addition, your perform ance makes yo"
    d += "u something of a local figure. When strangers recognize yo"
    d += "u in a town where you have performed, they typically take "
    d += "a liking to you."
    return d


def criminalContactDiscription() -> str:
    d = "You have a reliable and trustworthy contact who acts as you"
    d += "r liaison to a network of other criminals. You know how to"
    d += " get messages to and from your contact, even over great di"
    d += "stances; specifically, you know the local messengers, corr"
    d += "upt caravan masters, and seedy sailors who can deliver mes"
    d += "sages for you."
    return d


def citySecretsDiscription() -> str:
    d = "You know the secret patterns and flow to cities and can fin"
    d += "d passages through the urban sprawl that others would miss"
    d += ". When you are not in combat, you (and companions you lead"
    d += ") can travel between any two locations in the city twice a"
    d += "s fast as your speed would normally allow."
    return d


def discoveryDiscription() -> str:
    d = "The quiet seclusion of your extended hermitage gave you acc"
    d += "ess to a unique and powerful discovery. The exact nature o"
    d += "f this revelation depends on the nature of your seclusion."
    d += " It might be a great truth about the cosmos, the deities, "
    d += "the powerful beings of the outer planes, or the forces of "
    d += "nature. It could be a site that no one else has ever seen."
    d += " You might have uncovered a fact that has long been forgot"
    d += "ten, or unearthed some relic of the past that could rewrit"
    d += "e history. It might be information that would be damaging "
    d += "to the people who or consigned you to exile, and hence the"
    d += " reason for your return to society. Work with your DM to d"
    d += "etermine the details of your discovery and its impact on t"
    d += "he campaign."
    return d


def falseIdentityDiscription() -> str:
    d = "You have created a second identity that includes documentat"
    d += "ion, established acquaintances, and disguises that allow y"
    d += "ou to assume that persona. Additionally, you can forge doc"
    d += "uments including official papers and personal letters, as "
    d += "long as you have seen an example of the kind of document o"
    d += "r the handwriting you are trying to copy."
    return d


def guildMembershipDiscription() -> str:
    d = "As an established and respected member of a guild, you can " 
    d += "rely on certain benefits that membership provides. Your fe"
    d += "llow guild members will provide you with lodging and food "
    d += "if necessary, and pay for your funeral if needed. In some "
    d += "cities and towns, a guildhall offers a central place to me"
    d += "et other members of your profession, which can be a good p"
    d += "lace to meet potential patrons, allies, or hirelings. Guil"
    d += "ds often wield tremendous political power. If you are accu"
    d += "sed of a crime, your guild will support you if a good case"
    d += " can be made for your innocence or the crime is justifiabl"
    d += "e. You can also gain access to powerful political figures "
    d += "through the guild, if you are a member in good standing. S"
    d += "uch connections might require the donation of money or mag"
    d += "ic items to the guild’s coffers. You must pay dues of 5 gp"
    d += " per month to the guild. If you miss payments, you must ma"
    d += "ke up back dues to remain in the guild’s good graces."
    return d


def militaryRankDiscription() -> str:
    d = "You have a military rank from your career as a soldier. Sol"
    d += "diers loyal to your former military organization still rec"
    d += "ognize your authority and influence, and they defer to you"
    d += " if they are of a lower rank. You can invoke your rank to "
    d += "exert influence over other soldiers and requisition simple"
    d += " equipment or horses for temporary use. You can also usual"
    d += "ly gain access to friendly military encampments and fortre"
    d += "sses where your rank is recognized."
    return d


def positionOfPrivilegeDiscription() -> str:
    d = "Thanks to your noble birth, people are inclined to think th"
    d += "e best of you. You are welcome in high society, and people"
    d += " assume you have the right to be wherever you are. The com"
    d += "mon folk make every effort to accommodate you and avoid yo"
    d += "ur displeasure, and other people of high birth treat you a"
    d += "s a member of the same social sphere. You can secure an au"
    d += "dience with a local noble if you need to."
    return d


def researcherDiscription() -> str:
    d = "When you attempt to learn or recall a piece of lore, if yo"
    d += "u do not know that information, you often know where and f"
    d += "rom whom you can obtain it. Usually, this information come"
    d += "s from a library, scriptorium, university, or a sage or ot"
    d += "her learned person or creature. Your DM might rule that th"
    d += "e knowledge you seek is secreted away in an almost inacces"
    d += "sible place, or that it simply cannot be found. Unearthing"
    d += " the deepest secrets of the multiverse can require an adve"
    d += "nture or even a whole campaign."
    return d


def rusticHospitalityDiscription() -> str:
    d = "Since you com e from the ranks of the com m on folk, you fi"
    d += "t in among them with ease. You can find a place to hide, r"
    d += "est, or recuperate among other commoners, unless you have "
    d += "shown yourself to be a danger to them. They will shield yo"
    d += "u from the law or anyone else searching for you, though th"
    d += "ey will not risk their lives for you."
    return d


def shelterOfTheFaithfulDiscription() -> str:
    d = "As an acolyte, you command the respect of those who share y"
    d += "our faith, and you can perform the religious ceremonies of"
    d += " your deity. You and your adventuring companions can expec"
    d += "t to receive free healing and care at a temple, shrine, or"
    d += " other established presence of your faith, though you must"
    d += " provide any material components needed for spells. Those "
    d += "who share your religion will support you (but only you) at"
    d += " a modest lifestyle. You might also have ties to a specifi"
    d += "c temple dedicated to your chosen deity or pantheon, and y"
    d += "ou have a residence there. This could be the temple where "
    d += "you used to serve, if you remain on good terms with it, or"
    d += " a temple where you have found a new home. While near your"
    d += " temple, you can call upon the priests for assistance, pro"
    d += "vided the assistance you ask for is not hazardous and you "
    d += "remain in good standing with your temple."
    return d


def shipsPassageDiscription() -> str:
    d = "When you need to, you can secure free passage on a sailing "
    d += "ship for yourself and your adventuring companions. You mig"
    d += "ht sail on the ship you served on, or another ship you hav"
    d += "e good relations with (perhaps one captained by a former c"
    d += "rewmate). Because you’re calling in a favor, you can’t be "
    d += "certain of a schedule or route that will meet your every n"
    d += "eed. Your Dungeon Master will determine how long it takes "
    d += "to get where you need to go. In return for your free passa"
    d += "ge, you and your companions are expected to assist the cre"
    d += "w during the voyage."
    return d


def wandererDiscription() -> str:
    d = "You have an excellent m em ory for maps and geography, and "
    d += "you can always recall the general layout of terrain, settl"
    d += "ements, and other features around you. In addition, you ca"
    d += "n find food and fresh water for yourself and up to five ot"
    d += "her people each day, provided that the land offers berries"
    d += ", small game, water, and so forth."
    return d