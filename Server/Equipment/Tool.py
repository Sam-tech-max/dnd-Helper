import Equipment.Item as Item

class Tool(Item.Item):
	def __init__(self, name="Aichemist'supplies",
	toolType="Artisan's tools", cost=50, costType="gp", weight="8 lb"):
		super().__init__(name, toolType, cost, costType)
		self.weight = weight

	def printTool(self):
		super().printItem()
		print("Weight:", self.getWeight())
# //---------// //---------// //---------//
# Get and Set function statements
# //---------// //---------// //---------//
	def getWeight(self):
		return self.weight
		
	def setWeight(self, weight):
		self.weight = weight

# //---------// //---------// //---------//
# Main function statements
# //---------// //---------// //---------//
