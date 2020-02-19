class Item:
	def __init__(self, name: str = "meat, chunk",
			  itemType: str = "generic", cost: int = 3,
			  costType: str = "sp", amount: int = 1):
		self.name = name
		self.itemType = itemType
		self.cost = cost
		if(not(costType == "cp" or costType == "sp" or
		 costType == "ep" or costType == "gp" or costType == "pp")):
			print("Not one of the currency types")
			costType = "cp"
		self.costType = costType
		self.amount = amount

		
	def printItem(self):
		print("Item Name:", self.getName())
		print("Item Type:", self.getItemType())
		print("Cost:", self.getCost(), self.getCostType())
		if(self.getAmount() > 1):
			print("Amount:", self.getAmount())

# //---------// //---------// //---------//
# Get and Set statements
# //---------// //---------// //---------//
	def getAmount(self) -> int:
		return self.amount


	def setAmount(self, amount: int):
		if(amount > 0):
			self.amount = amount
		else:
			self.amount = 0


	def getCost(self):
		return self.cost
		
	def setCost(self, cost):
		self.cost = cost
		
	def getCostType(self):
		return self.costType
		
	def setCostType(self, costType):
		if(not(costType == "cp" or costType == "sp" or costType == "ep"
		or costType == "gp" or costType == "pp")):
			costType = "cp"
		self.costType = costType
		
	def getItemType(self):
		return self.itemType
		
	def setItemType(self, itemType):
		self.itemType = itemType
		
	def getName(self):
		return self.name
		
	def setName(self, name):
		self.name = name


def chooseTrinket() -> Item:
	trinket = str(input("Roll a d100 and enter the number: "))
	return getTrinketByNumber(trinket)


def getTrinketByNumber(trinket: str = 1) -> Item:
	if(trinket == "1"):
		return Item("mummified goblin hand", "trinket", 0, "gp", 1)
	elif(trinket == "2"):
		return Item("piece of crystal that faintly glows in the moonlight", "trinket", 0, "gp", 0)
	elif(trinket == "3"):
		return Item("gold coin minted in an unknown land", "trinket", 0, "gp", 1)
	elif(trinket == "4"):
		return Item("A diary written in a language you don’t know", "trinket", 0, "gp", 1)
	elif(trinket == "5"):
		return Item("A brass ring that never tarnishes", "trinket", 0, "gp", 1)
	elif(trinket == "6"):
		return Item("An old chess piece made from glass", "trinket", 0, "gp", 1)
	elif(trinket == "7"):
		return Item("A pair of knucklebone dice, each with a skull symbol on the side that would normally show six pips", "trinket", 0, "gp", 1)
	elif(trinket == "8"):
		return Item("A small idol depicting a nightmarish creature that gives you unsettling dreams when you sleep near it", "trinket", 0, "gp", 1)
	elif(trinket == "9"):
		return Item("A rope necklace from which dangles four mummified elf fingers", "trinket", 0, "gp", 1)
	elif(trinket == "10"):
		return Item("The deed for a parcel of land in a realm unknown to you", "trinket", 0, "gp", 1)
	elif(trinket == "11"):
		return Item("A 1-ounce block made from an unknown material", "trinket", 0, "gp", 1)
	elif(trinket == "12"):
		return Item("A small cloth doll skewered with needles", "trinket", 0, "gp", 1)
	elif(trinket == "13"):
		return Item("A tooth from an unknown beast", "trinket", 0, "gp", 1)
	elif(trinket == "14"):
		return Item("An enormous scale, perhaps from a dragon", "trinket", 0, "gp", 1)
	elif(trinket == "15"):
		return Item("A bright green feather", "trinket", 0, "gp", 1)
	elif(trinket == "16"):
		return Item("An old divination card bearing your likeness", "trinket", 0, "gp", 1)
	elif(trinket == "17"):
		return Item("A glass orb filled with moving smoke", "trinket", 0, "gp", 1)
	elif(trinket == "18"):
		return Item("A 1-pound egg with a bright red shell", "trinket", 0, "gp", 1)
	elif(trinket == "19"):
		return Item("A pipe that blows bubbles", "trinket", 0, "gp", 1)
	elif(trinket == "20"):
		return Item("A glass jar containing a weird bit of flesh floating in pickling fluid", "trinket", 0, "gp", 1)
	elif(trinket == "21"):
		return Item("A tiny gnome-crafted music box that plays a song you dimly remember from your childhood", "trinket", 0, "gp", 1)
	elif(trinket == "22"):
		return Item("A small wooden statuette of a smug halfling", "trinket", 0, "gp", 1)
	elif(trinket == "23"):
		return Item("A brass orb etched with strange runes", "trinket", 0, "gp", 1)
	elif(trinket == "24"):
		return Item("A multicolored stone disk", "trinket", 0, "gp", 1)
	elif(trinket == "25"):
		return Item("A tiny silver icon of a raven", "trinket", 0, "gp", 1)
	elif(trinket == "26"):
		return Item("A bag containing forty-seven humanoid teeth, one of which is rotten", "trinket", 0, "gp", 1)
	elif(trinket == "27"):
		return Item("A shard of obsidian that always feels warm to the touch", "trinket", 0, "gp", 1)
	elif(trinket == "28"):
		return Item("A dragon's bony talon hanging from a plain leather necklace", "trinket", 0, "gp", 1)
	elif(trinket == "29"):
		return Item("A pair of old socks", "trinket", 0, "gp", 1)
	elif(trinket == "30"):
		return Item("A blank book whose pages refuse to hold ink, chalk, graphite, or any other substance or marking", "trinket", 0, "gp", 1)
	elif(trinket == "31"):
		return Item("A silver badge in the shape of a five-pointed star", "trinket", 0, "gp", 1)
	elif(trinket == "32"):
		return Item("A knife that belonged to a relative", "trinket", 0, "gp", 1)
	elif(trinket == "33"):
		return Item("A glass vial filled with nail clippings", "trinket", 0, "gp", 1)
	elif(trinket == "34"):
		return Item("A rectangular metal device with two tiny metal cups on one end that throws sparks when wet", "trinket", 0, "gp", 1)
	elif(trinket == "35"):
		return Item("A white, sequined glove sized for a human", "trinket", 0, "gp", 1)
	elif(trinket == "36"):
		return Item("A vest with one hundred tiny pockets", "trinket", 0, "gp", 1)
	elif(trinket == "37"):
		return Item("A small, weightless stone block", "trinket", 0, "gp", 1)
	elif(trinket == "38"):
		return Item("A tiny sketch portrait of a goblin", "trinket", 0, "gp", 1)
	elif(trinket == "39"):
		return Item("An empty glass vial that smells of perfume when opened", "trinket", 0, "gp", 1)
	elif(trinket == "40"):
		return Item("A gemstone that looks like a lump of coal when examined by anyone but you", "trinket", 0, "gp", 1)
	elif(trinket == "41"):
		return Item("A scrap of cloth from an old banner", "trinket", 0, "gp", 1)
	elif(trinket == "42"):
		return Item("A rank insignia from a lost legionnaire", "trinket", 0, "gp", 1)
	elif(trinket == "43"):
		return Item("A tiny silver bell without a clapper", "trinket", 0, "gp", 1)
	elif(trinket == "44"):
		return Item("A mechanical canary inside a gnomish lamp", "trinket", 0, "gp", 1)
	elif(trinket == "45"):
		return Item("A tiny chest carved to look like it has numerous feet on the bottom", "trinket", 0, "gp", 1)
	elif(trinket == "46"):
		return Item("A dead sprite inside a clear glass bottle", "trinket", 0, "gp", 1)
	elif(trinket == "47"):
		return Item("A metal can that has no opening but sounds as if it is filled with liquid, sand, spiders, or broken glass (your choice)", "trinket", 0, "gp", 1)
	elif(trinket == "48"):
		return Item("A glass orb filled with water, in which swims a clockwork goldfish", "trinket", 0, "gp", 1)
	elif(trinket == "49"):
		return Item("A silver spoon with an M engraved on the handle", "trinket", 0, "gp", 1)
	elif(trinket == "50"):
		return Item("A whistle made from gold-colored wood", "trinket", 0, "gp", 1)
	elif(trinket == "51"):
		return Item("A dead scarab beetle the size of your hand", "trinket", 0, "gp", 1)
	elif(trinket == "52"):
		return Item("Two toy soldiers, one with a missing head", "trinket", 0, "gp", 1)
	elif(trinket == "53"):
		return Item("A small box filled with different-sized buttons", "trinket", 0, "gp", 1)
	elif(trinket == "54"):
		return Item("A candle that can’t be lit", "trinket", 0, "gp", 1)
	elif(trinket == "55"):
		return Item("A tiny cage with no door", "trinket", 0, "gp", 1)
	elif(trinket == "56"):
		return Item("An old key", "trinket", 0, "gp", 1)
	elif(trinket == "57"):
		return Item("An indecipherable treasure map", "trinket", 0, "gp", 1)
	elif(trinket == "58"):
		return Item("A hilt from a broken sword", "trinket", 0, "gp", 1)
	elif(trinket == "59"):
		return Item("A rabbit’s foot", "trinket", 0, "gp", 1)
	elif(trinket == "60"):
		return Item("A glass eye", "trinket", 0, "gp", 1)
	elif(trinket == "61"):
		return Item("A cameo carved in the likeness of a hideous person", "trinket", 0, "gp", 1)
	elif(trinket == "62"):
		return Item("A silver skull the size of a coin", "trinket", 0, "gp", 1)
	elif(trinket == "63"):
		return Item("An alabaster mask", "trinket", 0, "gp", 1)
	elif(trinket == "64"):
		return Item("A pyramid of sticky black incense that smells very bad", "trinket", 0, "gp", 1)
	elif(trinket == "65"):
		return Item("A nightcap that, when worn, gives you pleasant dreams", "trinket", 0, "gp", 1)
	elif(trinket == "66"):
		return Item("A single caltrop made from bone", "trinket", 0, "gp", 1)
	elif(trinket == "67"):
		return Item("A gold monocle frame without the lens", "trinket", 0, "gp", 1)
	elif(trinket == "68"):
		return Item("A 1-inch cube, each side painted a different color", "trinket", 0, "gp", 1)
	elif(trinket == "69"):
		return Item("A crystal knob from a door", "trinket", 0, "gp", 1)
	elif(trinket == "70"):
		return Item("A small packet filled with pink dust", "trinket", 0, "gp", 1)
	elif(trinket == "71"):
		return Item("A fragment of a beautiful song, written as musical notes on two pieces of parchment", "trinket", 0, "gp", 1)
	elif(trinket == "72"):
		return Item("A silver teardrop earring made from a real teardrop", "trinket", 0, "gp", 1)
	elif(trinket == "73"):
		return Item("The shell of an egg painted with scenes of human misery in disturbing detail", "trinket", 0, "gp", 1)
	elif(trinket == "74"):
		return Item("A fan that, when unfolded, shows a sleeping cat", "trinket", 0, "gp", 1)
	elif(trinket == "75"):
		return Item("A set of bone pipes", "trinket", 0, "gp", 1)
	elif(trinket == "76"):
		return Item("A four-leaf clover pressed inside a book discussing manners and etiquette", "trinket", 0, "gp", 1)
	elif(trinket == "77"):
		return Item("A sheet of parchment upon which is drawn a complex mechanical contraption", "trinket", 0, "gp", 1)
	elif(trinket == "78"):
		return Item("An ornate scabbard that fits no blade you have found so far", "trinket", 0, "gp", 1)
	elif(trinket == "79"):
		return Item("An invitation to a party where a murder happened", "trinket", 0, "gp", 1)
	elif(trinket == "80"):
		return Item("A bronze pentacle with an etching of a rat's head in its center", "trinket", 0, "gp", 1)
	elif(trinket == "81"):
		return Item("A purple handkerchief embroidered with the name of a powerful archmage", "trinket", 0, "gp", 1)
	elif(trinket == "82"):
		return Item("Half of a floorplan for a temple, castle, or some other structure", "trinket", 0, "gp", 1)
	elif(trinket == "83"):
		return Item("A bit of folded cloth that, when unfolded, turns into a stylish cap", "trinket", 0, "gp", 1)
	elif(trinket == "84"):
		return Item("A glass eye 84 A receipt of deposit at a bank in a far-flung city", "trinket", 0, "gp", 1)
	elif(trinket == "85"):
		return Item("A diary with seven missing pages", "trinket", 0, "gp", 1)
	elif(trinket == "86"):
		return Item("An empty silver snuffbox bearing an inscription on the surface that says “dreams’’", "trinket", 0, "gp", 1)
	elif(trinket == "87"):
		return Item("An iron holy symbol devoted to an unknown god", "trinket", 0, "gp", 1)
	elif(trinket == "88"):
		return Item("A book that tells the story of a legendary hero's rise and fall, with the last chapter missing", "trinket", 0, "gp", 1)
	elif(trinket == "89"):
		return Item("A vial of dragon blood", "trinket", 0, "gp", 1)
	elif(trinket == "90"):
		return Item("An ancient arrow of elven design", "trinket", 0, "gp", 1)
	elif(trinket == "91"):
		return Item("A needle that never bends", "trinket", 0, "gp", 1)
	elif(trinket == "92"):
		return Item("An ornate brooch of dwarven design", "trinket", 0, "gp", 1)
	elif(trinket == "93"):
		return Item("An empty wine bottle bearing a pretty label that says, 'The Wizard of Wines Winery, Red Dragon Crush, 331422-W'", "trinket", 0, "gp", 1)
	elif(trinket == "94"):
		return Item("A mosaic tile with a multicolored, glazed surface", "trinket", 0, "gp", 1)
	elif(trinket == "95"):
		return Item("A petrified mouse", "trinket", 0, "gp", 1)
	elif(trinket == "96"):
		return Item("A black pirate flag adorned with a dragon's skull and crossbones", "trinket", 0, "gp", 1)
	elif(trinket == "97"):
		return Item("A tiny mechanical crab or spider that moves about when it’s not being observed", "trinket", 0, "gp", 1)
	elif(trinket == "98"):
		return Item("A glass jar containing lard with a label that reads, 'Griffon Grease'", "trinket", 0, "gp", 1)
	elif(trinket == "99"):
		return Item("A wooden box with a ceramic bottom that holds a living worm with a head on each end of its body", "trinket", 0, "gp", 1)
	else:
		return Item("A metal urn containing the ashes of a hero", "trinket", 0, "gp", 1)


def chooseAnimalTrophy() -> Item:
	return Item(str(input("Enter a animal trophy: ")), "anmial trophy", 0, "gp", 1)


def chooseFallenEnemyTrophy() -> Item:
	return Item(str(input("Enter a fallen enemy trophy: ")), "fallen enemy trophy", 0, "gp", 1)

# //---------// //---------// //---------//
# Main function statements
# //---------// //---------// //---------//
