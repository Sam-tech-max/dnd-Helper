import Tool

class Weapon(Tool.Tool):
	def __init__(self, name="Club", weaponType="Simple Melee Weapon",
	cost=1, costType="sp", damage="1d4", damageType="bludgeoning",
	weight="2 lb", properties="Light"):
		super().__init__(name, weaponType, cost, costType, weight)
		self.damage = damage
		self.damageType = damageType
		self.properties =properties
		
	def printWeapon(self):
		super().printTool()
		print("Damage:", self.getDamage(), self.getDamageType())
		print("Properties:", self.getProperties())
		
		
# //---------// //---------// //---------//
# Get and Set function statements
# //---------// //---------// //---------//
	def getDamage(self):
		return self.damage
		
	def setDamage(self, damage):
		self.damage = damage
		
	def getDamageType(self):
		return self.damageType
		
	def setDamageType(self, damageType):
		self.damageType = damageType
		
	def getProperties(self):
		return self.properties
		
	def setProperties(self, properties):
		self.properties = properties

# //---------// //---------// //---------//
# Main function statements
# //---------// //---------// //---------//
