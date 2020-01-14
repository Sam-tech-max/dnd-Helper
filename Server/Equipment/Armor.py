import Tool

class Armor(Tool.Tool):
	def __init__(self, name="Padded", armorType="Light Armor",
	cost=5, costType="gp", armorClass="11 + Dex modifier",
	strength="null", disadvantageOnStealth=True, weight="2 lb"):
		super().__init__(name, armorType, cost, costType, weight)
		self.armorClass = armorClass
		self.strength = strength
		self.disadvantageOnStealth = disadvantageOnStealth
				
	def printArmor(self):
		super().printTool()
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
