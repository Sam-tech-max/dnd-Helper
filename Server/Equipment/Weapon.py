import Equipment.Tool as Tool

class Weapon(Tool.Tool):
	def __init__(self, name: str ="Club", weaponType: str = "Simple Melee Weapon",
	cost: int = 1, costType: str = "sp", damage: str = "1d4", damageType: str = "bludgeoning",
	weight: int = 2, properties: str = "Light", amount: int = 1):
		super().__init__(name, weaponType, cost, costType, weight, amount)
		self.damage = damage
		self.damageType = damageType
		self.properties =properties
		
	def printItem(self):
		super().printTool()
		print("Damage:", self.getDamage(), self.getDamageType())
		print("Properties:", self.getProperties())
		
		
# //---------// //---------// //---------//
# Get and Set function statements
# //---------// //---------// //---------//
	def getDamage(self) -> str:
		return self.damage
		
	def setDamage(self, damage: str):
		self.damage = damage
		
	def getDamageType(self) -> str:
		return self.damageType
		
	def setDamageType(self, damageType: str):
		self.damageType = damageType
		
	def getProperties(self) -> str:
		return self.properties
		
	def setProperties(self, properties: str):
		self.properties = properties

# //---------// //---------// //---------//
# Main function statements
# //---------// //---------// //---------//
