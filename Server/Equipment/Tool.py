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
# //---------// //---------// //---------//
# Main function statements
# //---------// //---------// //---------//
