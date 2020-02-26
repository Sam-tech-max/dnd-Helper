import Equipment.Item as Item


class Tool(Item.Item):
	def __init__(self, name: str = "Aichemist'supplies",
			  toolType: str ="Artisan's tools", cost: int = 50,
			  costType: str = "gp", weight: int = 8,
			  amount: int = 1):
		super().__init__(name, toolType, cost, costType, amount)
		self.weight = weight

	def printItem(self):
		super().printItem()
		print("Weight:", self.getWeight(), "lb")
# //---------// //---------// //---------//
# Get and Set function statements
# //---------// //---------// //---------//
	def getWeight(self):
		return self.weight
		
	def setWeight(self, weight):
		self.weight = weight

# //---------// //---------// //---------//
# Function statements associated with
# the Backgrounds
# //---------// //---------// //---------//
def chooseHolySymbol() -> Tool:
	print("Choose Holy Symbol: ")
	print("Enter 1: Amulet")
	print("Enter 2: Emblem")
	print("Enter 3: Reliquary")
	holySymbol = str(input())
	if(holySymbol == "1"):
		return Tool("amulet", "holy symbol", 5, "gp", 1)
	elif(holySymbol == "2"):
		return Tool("emblem", "holy symbol", 5, "gp", 0)
	elif(holySymbol == "3"):
		return Tool("reliquary", "holy symbol", 5, "gp", 2)
	else:
		print("Not a valid Holy Symbol!")
		return chooseHolySymbol()

def chooseConTool() -> Tool:
	print("Choose Con Tool:")
	print("Enter 1: 10 stoppered bottles filled with colored liquid")
	print("Enter 2: a set of weighted dice")
	print("Enter 3: a deck of marked cards")
	print("Enter 4: a signet ring of an imaginary duke")
	conTool = str(input())
	if(conTool == "1"):
		return Tool("stoppered bottles filled with colored liquid", "con tool", 0, "gp", 0, 10)
	elif(conTool == "2"):
		return Tool("weighted dice set", "gaming", 1, "sp", 0, 1)
	elif(conTool == "3"):
		return Tool("deck of marked cards", "con tool", 5, "sp", 0, 1)
	elif(conTool == "4"):
		return Tool("a signet ring of an imaginary duke", "con tool", 5, "gp", 0, 1)
	else:
		print("Not a valid Con Tool")
		return chooseConTool()


def chooseMusicalInstruments() -> Tool:
	print("Choose Musical Instrument:")
	print("Enter 1: Bagpipes")
	print("Enter 2: Drum")
	print("Enter 3: Duicimer")
	print("Enter 4: Flute")
	print("Enter 5: Lute")
	print("Enter 6: Lyre")
	print("Enter 7: Horn")
	print("Enter 8: Pan flute")
	print("Enter 9: Shawm")
	print("Enter 10: Viol")
	musIns = str(input())
	if(musIns == "1"):
		return Tool("bagpipes", "musical instrument", 30, "gp", 6, 1)
	elif(musIns == "2"):
		return Tool("drum", "musical instrument", 6, "gp", 3, 1)
	elif(musIns == "3"):
		return Tool("dulcimer", "musical instrument", 25, "gp", 10, 1)
	elif(musIns == "4"):
		return Tool("flute", "musical instrument", 2, "gp", 1, 1)
	elif(musIns == "5"):
		return Tool("lute", "musical instrument", 35, "gp", 2, 1)
	elif(musIns == "6"):
		return Tool("lyre", "musical instrument", 30, "gp", 2, 1)
	elif(musIns == "7"):
		return Tool("horn", "musical instrument", 3, "gp", 2, 1)
	elif(musIns == "8"):
		return Tool("pan flute", "musical instrument", 12, "gp", 2, 1)
	elif(musIns == "9"):
		return Tool("shawm", "musical instrument", 2, "gp", 1, 1)
	elif(musIns == "10"):
		return Tool("viol", "musical instrument", 30, "gp", 1, 1)
	else:
		print("Not a valid Musical Instrument")
		return chooseMusicalInstruments()

def chooseArtisanTool() -> Tool:
	print("Choose an Artisan tool:")
	print("Enter 1: aichemist's supplies")
	print("Enter 2: brewer's supplies")
	print("Enter 3: caligrapher's supplies")
	print("Enter 4: carpenter's tools")
	print("Enter 5: cartographer's tools")
	print("Enter 6: cobbler's tools")
	print("Enter 7: cook's utensils")
	print("Enter 8: glassblower's tools")
	print("Enter 9: jeweler's tools")
	print("Enter 10: leatherworker's tools")
	print("Enter 11: mason's tools")
	print("Enter 12: painter's supplies")
	print("Enter 13: potter's tools")
	print("Enter 14: smith's tools")
	print("Enter 15: tinker's tools")
	print("Enter 16: weaver's tools")
	print("Enter 17: woodcarver's tools")
	artTool = str(input())
	if(artTool == "1"):
		return Tool("Alchemist’s supplies", "artisan's tools", 50, "gp", 8, 1)
	elif(artTool == "2"):
		return Tool("Brewer’s supplies", "artisan's tools", 20, "gp", 9, 1)
	elif(artTool == "3"):
		return Tool("Calligrapher's supplies", "artisan's tools", 10, "gp", 5, 1)
	elif(artTool == "4"):
		return Tool("Carpenter’s tools", "artisan's tools", 8, "gp", 6, 1)
	elif(artTool == "5"):
		return Tool("Cartographer’s tools", "artisan's tools", 15, "gp", 6, 1)
	elif(artTool == "6"):
		return Tool("Cobbler’s tools", "artisan's tools", 5, "gp", 5, 1)
	elif(artTool == "7"):
		return Tool("Cook’s utensils", "artisan's tools", 1, "gp", 8, 1)
	elif(artTool == "8"):
		return Tool("Glassblower’s tools", "artisan's tools", 30, "gp", 5, 1)
	elif(artTool == "9"):
		return Tool("Jeweler’s tools", "artisan's tools", 25, "gp", 2, 1)
	elif(artTool == "10"):
		return Tool("Leatherworker’s tools", "artisan's tools", 5, "gp", 5, 1)
	elif(artTool == "11"):
		return Tool("Mason’s tools", "artisan's tools", 10, "gp", 8, 1)
	elif(artTool == "12"):
		return Tool("Painter’s supplies", "artisan's tools", 10, "gp", 5, 1)
	elif(artTool == "13"):
		return Tool("Potter’s tools", "artisan's tools", 10, "gp", 3, 1)
	elif(artTool == "14"):
		return Tool("Smith’s tools", "artisan's tools", 20, "gp", 8, 1)
	elif(artTool == "15"):
		return Tool("Tinker’s tools", "artisan's tools", 50, "gp", 10, 1)
	elif(artTool == "16"):
		return Tool("Weaver’s tools", "artisan's tools", 1, "gp", 5, 1)
	elif(artTool == "17"):
		return Tool("Woodcarver's tools", "artisan's tools", 1, "gp", 5, 1)
	else:
		print("Not an Artisan's tools")
		return chooseArtisanTool()

def chooseGamingSet(solider: bool = False):
	print("Choose a gaming set:")
	print("Enter 1: deck of cards")
	if(not solider):
		print("Enter 2: dragonchess set")
		print("Enter 3: three-dragon ante set")
		print("Enter 4: dice set")
		gameSet = str(input())
		if(gameSet == "1"):
			return Tool("deck of cards", "gaming set", 5, "sp", 0, 1)
		elif(gameSet == "2"):
			return Tool("dragonchess set", "gaming set", 1, "gp", 0, 1)
		elif(gameSet == "3"):
			return Tool("three-dragon ante set", "gaming set", 1, "gp", 0, 1)
		elif(gameSet == "4"):
			return Tool("dice set", "gaming set", 1, "sp", 0, 1)
	else:
		print("Enter 2: bone dice")
		gameSet = str(input())
		if(gameSet == "1"):
			return Tool("deck of cards", "gaming set", 5, "sp", 0, 1)
		elif(gameSet == "2"):
			return Tool("bone dice set", "gaming set", 1, "sp", 0, 1)
	print("Not a valid gaming set")
	return chooseGamingSet(solider)


def getToolByName(name: str = "abacus", amount: int = 1) -> Tool:
	if(name == "abacus"):
		return Tool("abacus", "generic", 2, "gp", 2, amount)
	elif(name == "acid (vial)"):
		return Tool("acid (vial)", "generic", 25, "gp", 1, amount)
	elif(name == "alchemist's fire (flask)"):
		return Tool("alchemist’s fire (flask)", "generic", 50, "gp", 1, amount)
	elif(name == "arrow (20)"):
		return Tool("arrows", "ammunition", 5, "cp", 1, 20 * amount)
	elif(name == "arrow"):
		return Tool("arrows", "ammunition", 5, "cp", 1, amount)
	elif(name == "blowgun needles (50)"):
		return Tool("blowgun needles", "ammunition", 5, "cp", 1, 50*amount)
	elif(name == "blowgun needles"):
		return Tool("blowgun needles", "ammunition", 5, "cp", 1, amount)
	elif(name == "crossbow bolts (20)"):
		return Tool("crossbow bolts", "ammunition",1, "gp", 1 + 1/2, 20*amount)
	elif(name == "crossbow bolts"):
		return Tool("crossbow bolts", "ammunition",1, "gp", 1 + 1/2, amount)
	elif(name == "sling bullets (20)"):
		return Tool("sling bullet", "ammunition", 4, "cp", 1 + 1/2, amount)
	elif(name == "antitoxin (vial)"):
		return Tool("antitoxin (vial)", "generic", 50, "gp", 0, amount)
	elif(name == "crystal"):
		return Tool("crystal", "arcane focus", 10, "gp", 1, amount)
	elif(name == "orb"):
		return Tool("orb", "arcane focus", 20, "gp", 3, amount)
	elif(name == "rod"):
		return Tool("rod", "arcane focus", 10, "gp", 2, amount)
	elif(name == "staff"):
		return Tool("staff", "arcane focus", 5, "gp", 4, amount)
	elif(name == "wand"):
		return Tool("wand", "arcane focus", 10, "gp", 1, amount)
	elif(name == "backpack"):
		return Tool("backpack", "generic", 2, "gp",5, amount)
	elif(name == "ball bearings (bag of 1000)"):
		return Tool("ball bearings (bag of 1000)", "generic", 1, "gp", 2, amount)
	elif(name == "barrel"):
		return Tool("barrel", "generic", 2, "gp", 70, amount)
	elif(name == "basket"):
		return Tool("basket", "generic", 4, "sp", 2, amount)
	elif(name == "bedroll"):
		return Tool("bedroll", "generic", 1, "gp", 7, amount)
	elif(name == "bell"):
		return Tool("bell", "generic", 1, "gp", 0, amount)
	elif(name == "blanket"):
		return Tool("blanket", "generic", 5, "sp", 3, amount)
	elif(name == "block and tackle"):
		return Tool("block and tackle", "generic", 1, "gp", 5, amount)
	elif(name == "book"):
		return Tool("book", "generic", 25, "gp", 5, amount)
	elif(name == "glass bottle"):
		return Tool("glass bottle", "generic", 2, "gp", 2, amount)
	elif(name == "bucket"):
		return Tool("bucket", "generic", 5, "cp", 2, amount)
	elif(name == "caltrops (bag of 20)"):
		return Tool("caltrops (bag of 20)", "generic", 1, "gp", 2, amount)
	elif(name == "candle"):
		return Tool("candle", "generic", 1, "cp", 0, amount)
	elif(name == "crossbow bolt case"):
		return Tool("crossbow bolt case", "generic", 1, "gp", 1, amount)
	elif(name == "map case"):
		return Tool("map case", "generic", 1, "gp", 1, amount)
	elif(name == "scroll case"):
		return Tool("scroll case", "generic", 1, "gp", 1, amount)
	elif(name == "chain (10 feet)"):
		return Tool("chain (10 feet)", "generic", 5, "gp", 10, amount)
	elif(name == "chalk"):
		return Tool("chalk", "generic", 1, "cp", 0, amount)
	elif(name == "chest"):
		return Tool("chest", "generic", 5, "gp", 25, amount)
	elif(name == "climber's kit"):
		return Tool("climber's kit", "generic", 25, "gp", 12, amount)
	elif(name == "common clothes"):
		return Tool("common clothes", "generic", 5, "sp", 3, amount)
	elif(name == "costume clothes"):
		return Tool("costume clothes", "generic", 5, "gp", 4, amount)
	elif(name == "fine clothes"):
		return Tool("fine clothes", "generic", 15, "gp", 6, amount)
	elif(name == "traveler's clothes"):
		return Tool("traveler's clothes", "generic", 2, "gp", 4, amount)
	elif(name == "component pouch"):
		return Tool("component pouch", "generic", 25, "gp", 2, amount)
	elif(name == "crowbar"):
		return Tool("crowbar", "generic", 2, "gp", 5, amount)
	elif(name == "sprig of mistletoe"):
		return Tool("sprig of mistletoe", "druidic focus", 1, "gp", 0, amount)
	elif(name == "totem"):
		return Tool("totem", "druidic focus", 1, "gp", 0, amount)
	elif(name == "wooden staff"):
		return Tool("wooden staff", "druidic focus", 5, "gp", 4, amount)
	elif(name == "yew wand"):
		return Tool("yew wand", "druidic focus", 10, "gp", 1, amount)
	elif(name == "fishing tackle"):
		return Tool("fishing tackle", "generic", 1, "gp", 4, amount)
	elif(name == "flask"):
		return Tool("flask", "generic", 2, "cp", 1, amount)
	elif(name == "tankard"):
		return Tool("tankard", "generic", 2, "cp", 1, amount)
	elif(name == "grappling hook"):
		return Tool("grappling hook", "generic", 2, "gp", 4, amount)
	elif(name == "hammer"):
		return Tool("hammer", "generic", 1, "gp", 3, amount)
	elif(name == "sledge hammer"):
		return Tool("sledge hammer", "generic", 2, "gp", 10, amount)
	elif(name == "healer's kit"):
		return Tool("healer’s kit", "generic", 5, "gp", 3, amount)
	elif(name == "amulet"):
		return Tool("amulet", "holy symbol", 5, "gp", 1, amount)
	elif(name == "emblem"):
		return Tool("emblem", "holy symbol", 5, "gp", 0, amount)
	elif(name == "reliquary"):
		return Tool("reliquary", "holy symbol", 5, "gp", 2, amount)
	elif(name == "holy water (flask)"):
		return Tool("holy water (flask)", "generic", 25, "gp", 1, amount)
	elif(name == "hourglass"):
		return Tool("hourglass", "generic", 25, "gp", 1, amount)
	elif(name == "hunting trap"):
		return Tool("hunting trap", "generic", 5, "gp", 25, amount)
	elif(name == "ink (1 ounce bottle)"):
		return Tool("ink (1 ounce bottle)", "generic", 10, "gp", 0, amount)
	elif(name == "ink pen"):
		return Tool("ink pen", "generic", 2, "cp", 0, amount)
	elif(name == "jug"):
		return Tool("jug", "generic", 2, "cp", 4, amount)
	elif(name == "pitcher"):
		return Tool("pitcher", "generic", 2, "cp", 4, amount)
	elif(name == "ladder (10-foot)"):
		return Tool("ladder (10-foot)", "generic", 1, "sp", 25, amount)
	elif(name == "lamp"):
		return Tool("lamp", "generic", 5, "sp", 1, amount)
	elif(name == "bullseye lantern"):
		return Tool("bullseye lantern", "generic", 10, "gp", 2, amount)
	elif(name == "hooded lantern"):
		return Tool("hooded lantern", "generic", 5, "gp",2, amount)
	elif(name == "lock"):
		return Tool("lock", "generic", 10, "gp", 1, amount)
	elif(name == "magnifying glass"):
		return Tool("magnifying glass", "generic", 100, "gp", 0, amount)
	elif(name == "manacles"):
		return Tool("manacles", "generic", 2, "gp", 6, amount)
	elif(name == "mess kit"):
		return Tool("mess kit", "generic", 2, "sp", 1, amount)
	elif(name == "steel mirror"):
		return Tool("steel mirror", "generic", 5, "gp", 1/2, amount)
	elif(name == "oil (flask)"):
		return Tool("oil (flask)", "generic", 1, "sp", 1, amount)
	elif(name == "paper"):
		return Tool("paper", "generic", 2, "sp", 0, amount)
	elif(name == "parchment"):
		return Tool("parchment", "generic", 1, "sp", 0, amount)
	elif(name == "perfume (vial)"):
		return Tool("perfume (vial)", "generic", 5, "gp", 0, amount)
	elif(name == "miner's pick"):
		return Tool("miner's pick", "generic", 2, "gp", 10, amount)
	elif(name == "piton"):
		return Tool("piton", "generic", 5, "cp", 1/4, amount)
	elif(name == "basic (vial) poison"):
		return Tool("basic (vial) poison", "generic", 100, "gp", 0, amount)
	elif(name == "pole (10-foot)"):
		return Tool("pole (10-foot)", "generic", 5, "cp", 7, amount)
	elif(name == "iron pot"):
		return Tool("iron pot", "generic", 2, "gp", 10, amount)
	elif(name == "potion of healing"):
		return Tool("potion of healing", "generic", 50, "gp", 1/2, amount)
	elif(name == "pouch"):
		return Tool("pouch", "generic", 5, "sp", 1, amount)
	elif(name == "quiver"):
		return Tool("quiver", "generic", 1, "gp", 1, amount)
	elif(name == "portable ram"):
		return Tool("portable ram", "generic", 4, "gp", 35, amount)
	elif(name == "ration"):
		return Tool("ration", "generic", 5, "sp", 2, amount)
	elif(name == "robes"):
		return Tool("robes", "generic", 1, "gp", 4, amount)
	elif(name == "hempen rope (50 feet)"):
		return Tool("hempen rope (50 feet)", "generic", 1, "gp", 10, amount)
	elif(name == "silk rope (50 feet)"):
		return Tool("silk rope (50 feet)", "generic", 10, "gp", 5, amount)
	elif(name == "sack"):
		return Tool("sack", "generic", 1, "cp", 1/2, amount)
	elif(name == ""):
		return Tool("merchant's scale", "generic", 5, "gp", 3, amount)
	elif(name == "sealing wax"):
		return Tool("sealing wax", "generic", 5, "sp", 0, amount)
	elif(name == "shovel"):
		return Tool("shovel", "generic", 2, "gp", 5, amount)
	elif(name == "signal whistle"):
		return Tool("signal whistle", "generic", 5, "cp", 0, amount)
	elif(name == "signet ring"):
		return Tool("signet ring", "generic", 5, "gp", 0, amount)
	elif(name == "soap"):
		return Tool("soap", "generic", 2, "cp", 0, amount)
	elif(name == "spellbook"):
		return Tool("spellbook", "generic", 50, "gp", 3, amount)
	elif(name == "iron spikes (10)"):
		return Tool("iron spike", "generic", 1, "gp", 1/2, 10*amount)
	elif(name == "iron spikes"):
		return Tool("iron spike", "generic", 1, "gp", 1/2, amount)
	elif(name == ""):
		return Tool("spyglass", "generic", 1000, "gp", 1, amount)
	elif(name == "two-person tent"):
		return Tool("two-person tent", "generic", 2, "gp", 20, amount)
	elif(name == "tinderbox"):
		return Tool("tinderbox", "generic", 5, "sp", 1, amount)
	elif(name == "torch"):
		return Tool("torch", "generic", 1, "cp", 1, amount)
	elif(name == "vial"):
		return Tool("vial", "generic", 1, "gp", 0, amount)
	elif(name == "waterskin"):
		return Tool("waterskin", "generic", 2, "sp", 5, amount)
	elif(name == "whetstone"):
		return Tool("whetstone", "generic", 1, "cp", 1, amount)
	elif(name == "alchemist's supplies"):
		return Tool("alchemist’s supplies", "artisan’s tools", 50, "gp", 8, amount)
	elif(name == "brewer's supplies"):
		return Tool("brewer’s supplies", "artisan’s tools", 20, "gp", 9, amount)
	elif(name == "calligrapher's supplies"):
		return Tool("calligrapher's supplies", "artisan’s tools", 10, "gp", 5, amount)
	elif(name == "carpenter's tools"):
		return Tool("carpenter’s tools", "artisan’s tools", 8, "gp", 6, amount)
	elif(name == "cartographer's tools"):
		return Tool("cartographer’s tools", "artisan’s tools", 15, "gp", 6, amount)
	elif(name == "cobbler's tools"):
		return Tool("cobbler’s tools", "artisan’s tools", 5, "gp", 5, amount)
	elif(name == "cook's utensils"):
		return Tool("cook’s utensils", "artisan’s tools", 1, "gp", 8, amount)
	elif(name == "glassblower's tools"):
		return Tool("glassblower’s tools", "artisan’s tools", 30, "gp", 5, amount)
	elif(name == "jeweler's tools"):
		return Tool("jeweler’s tools", "artisan’s tools", 25, "gp", 2, amount)
	elif(name == "leatherworker's tools"):
		return Tool("leatherworker’s tools", "artisan’s tools", 5, "gp", 5, amount)
	elif(name == "mason's tools"):
		return Tool("mason’s tools", "artisan’s tools", 10, "gp", 8, amount)
	elif(name == "painter's supplies"):
		return Tool("painter’s supplies", "artisan’s tools", 10, "gp", 5, amount)
	elif(name == "potter's tools"):
		return Tool("potter’s tools", "artisan’s tools", 10, "gp", 3, amount)
	elif(name == "smith's tools"):
		return Tool("smith’s tools", "artisan’s tools", 20, "gp", 8, amount)
	elif(name == "tinker's tools"):
		return Tool("tinker’s tools", "artisan’s tools", 50, "gp", 10, amount)
	elif(name == "weaver's tools"):
		return Tool("weaver’s tools", "artisan’s tools", 1, "gp", 5, amount)
	elif(name == "woodcarver's tools"):
		return Tool("woodcarver's tools", "artisan’s tools", 1, "gp", 5, amount)
	elif(name == "disguise kit"):
		return Tool("disguise kit", "generic", 25, "gp", 3, amount)
	elif(name == "forgery kit"):
		return Tool("forgery kit", "generic", 15, "gp", 5, amount)
	elif(name == "dice set"):
		return Tool("dice set", "gaming set", 1, "sp", 0, amount)
	elif(name == "dragonchess set"):
		return Tool("dragonchess set", "gaming set", 1, "gp", 1/2, amount)
	elif(name == "playing card set"):
		return Tool("playing card set", "gaming set", 5, "sp", 0, amount)
	elif(name == "three-dragon ante set"):
		return Tool("three-dragon ante set", "gaming set", 1, "gp", 0, amount)
	elif(name == "herbalism kit"):
		return Tool("herbalism kit", "generic", 5, "gp", 3, amount)
	elif(name == "bagpipes"):
		return Tool("bagpipes", "musical instrument", 30, "gp", 6, amount)
	elif(name == "drum"):
		return Tool("drum", "musical instrument", 6, "gp", 3, amount)
	elif(name == "dulcimer"):
		return Tool("dulcimer", "musical instrument", 25, "gp", 10, amount)
	elif(name == "flute"):
		return Tool("flute", "musical instrument", 2, "gp", 1, amount)
	elif(name == "lute"):
		return Tool("lute", "musical instrument", 35, "gp", 2, amount)
	elif(name == "lyre"):
		return Tool("lyre", "musical instrument", 30, "gp", 2, amount)
	elif(name == "horn"):
		return Tool("horn", "musical instrument", 3, "gp", 2, amount)
	elif(name == "pan flute"):
		return Tool("pan flute", "musical instrument", 12, "gp", 2, amount)
	elif(name == "shawm"):
		return Tool("shawm", "musical instrument", 2, "gp", 1, amount)
	elif(name == "viol"):
		return Tool("viol", "musical instrument", 30, "gp", 1, amount)
	elif(name == "navigator's tools"):
		return Tool("navigator’s tools", "generic", 25, "gp", 2, amount)
	elif(name == "poisoner's kit"):
		return Tool("poisoner’s kit", "generic", 50, "gp", 2, amount)
	elif(name == "thieves' tools"):
		return Tool("thieves’ tools", "generic", 25, "gp", 1, amount)

			
# //---------// //---------// //---------//
# Main function statements
# //---------// //---------// //---------//
