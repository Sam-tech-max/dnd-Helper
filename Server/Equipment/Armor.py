import Equipment.Tool as Tool

class Armor(Tool.Tool):
	def __init__(self,
			  name: str = "Padded",
			  armorType: str = "Light Armor",
			  cost: int = 5,
			  costType: str = "gp",
			  armorClass: str = "11 + Dex modifier",
			  strength: str = "null",
			  disadvantageOnStealth: bool = True,
			  weight: int = 2,
			  amount: int = 0):
		super().__init__(name, armorType, cost, costType, weight,
				   amount)
		self.armorClass = armorClass
		self.strength = strength
		self.disadvantageOnStealth = disadvantageOnStealth
				
	def printItem(self):
		super().printItem()
		print("Armor Class:", self.getArmorClass())
		print("Strength:", self.getStrength())
		if(self.getDisadvantageOnStealth()):
			print("Has a Disadvantage on stealth")
		
		
# //---------// //---------// //---------//
# Get and Set function statements
# //---------// //---------// //---------//
	def getArmorClass(self):
		return self.armorClass
		
	def setArmorClass(self, armorClass):
		self.armorClass = armorClass
		
	def getStrength(self):
		return self.strength
		
	def setStrength(self, strength):
		self.strength = strength
		
	def getDisadvantageOnStealth(self):
		return self.disadvantageOnStealth
		
	def setDisadvantageOnStealth(self, disadvantageOnStealth):
		self.disadvantageOnStealth = disadvantageOnStealth

# //---------// //---------// //---------//
# Main function statements
# //---------// //---------// //---------//
