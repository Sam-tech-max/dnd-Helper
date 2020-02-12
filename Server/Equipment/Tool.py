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
# //---------// //---------// //---------//
# Main function statements
# //---------// //---------// //---------//
