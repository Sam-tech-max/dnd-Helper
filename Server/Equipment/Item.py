class Item:
	def __init__(self, name="meat, chunk", itemType="generic", cost=3, costType="sp"):
		self.name = name
		self.itemType = itemType
		self.cost = cost
		if(not(costType == "cp" or costType == "sp" or costType == "ep"
		or costType == "gp" or costType == "pp")):
			print("Not one of the currency types")
			costType = "cp"
		self.costType = costType
		
	def printItem(self):
		print("Item Name:", self.getName())
		print("Item Type:", self.getItemType())
		print("Cost:", self.getCost(), self.getCostType())

# //---------// //---------// //---------//
# Get and Set statements
# //---------// //---------// //---------//
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

# //---------// //---------// //---------//
# Main function statements
# //---------// //---------// //---------//
item = Item()
item.setCostType("pp")
item.printItem()
