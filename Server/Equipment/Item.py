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

# //---------// //---------// //---------//
# Main function statements
# //---------// //---------// //---------//
