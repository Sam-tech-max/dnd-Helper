import Equipment.Tool as Tool

class Weapon(Tool.Tool):
	def __init__(self, name: str ="Club", weaponType: str = "Simple Melee Weapon",
	cost: int = 1, costType: str = "gp", damage: str = "1d4", damageType: str = "bludgeoning",
	weight: int = 2, properties: str = "Light", amount: int = 1):
		super().__init__(name, weaponType, cost, costType, weight, amount)
		self.damage = damage
		self.damageType = damageType
		self.properties =properties
		
	def printItem(self):
		super().printItem()
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
# function statements associated with classes
# //---------// //---------// //---------//
def getSimpleMeleeByName(name: str = "club", amount: int = 1) -> Weapon:
	name = name.lower()
	if(name == "club"):
		return Weapon("club", "simple melee", 1, "sp", "1d4",
				"bludgeoning", 2, "light", amount)
	elif(name == "dagger"):	
		return Weapon("dagger", "simple melee", 2, "gp", "1d4",
				"piercing", 1,"finesse light thrown (range 20/60))")
	elif(name == "greatclub"):
		return Weapon("greatclub", "simple melee",2, "sp", "1d8",
				"bludgeoning", 10, "Two-handed", amount)
	elif(name == "handaxe"):
		return Weapon("handaxe", "simple melee",5, "gp", "1d6",
				"slashing", 2, "light thrown (range 20/60)", amount)
	elif(name == "javelin"):
		return Weapon("javelin", "simple melee", 5, "sp", "1d6",
				"piercing", 2, "thrown (range 30/120)", amount)
	elif(name == "light hammer"):
		return Weapon("light hammer", "simple melee", 2, "gp", "1d4",
				"bludgeoning", 2, "light thrown (range 20/60)", amount)
	elif(name == "mace"):
		return Weapon("mace", "simple melee", 5, "gp", "1d6",
				"bludgeoning", 4, "null", amount)
	elif(name == "quarterstaff"):
		return Weapon("quarterstaff", "simple melee", 2, "sp", "1d6",
				"bludgeoning", 4,"versatile (1d8)", amount)
	elif(name == "sickle"):
		return Weapon("sickle", "simple melee", 1, "gp", "1d4",
				"slashing", 2, "light", amount)
	elif(name == "spear"):
		return Weapon("spear", "simple melee", 1, "gp", "1d6",
				"piercing", 3, "thrown (range 20/60) versatile (1d8)", amount)
	elif(name == "unarmed strike"):
		return Weapon("unarmed strike", "simple melee", 0, "gp", 1,
				"bludgeoning", 0, "null", amount)


def getSimpleRangedByName(name: str = "crossbow") -> Weapon:
	name = name.lower()
	if(name == "light crossbow"):
		return Weapon("light crossbow", "simple ranged", 25, "gp",
				"1d8", "piercing", 5,
				"ammunition (range 80/320) loading two-handed")
	elif(name == "dart"):
		return Weapon("dart", "simple ranged", 5, "cp", "1d4",
				"piercing", 1/4, "finesse thrown (range 20/60)")
	elif(name == "shortbow"):
		return Weapon("shortbow", "simple ranged", 25, "gp", "1d6",
				"piercing", 2,
				"ammunition (range 80/320) two-handed")
	elif(name == "sling"):
		return Weapon("sling", "simple ranged", 1, "sp", "1d4",
				"bludgeoning", 0, "ammunition (range 30/120)")


def getMartialMeleeByName(name: str = "battleaxe"):
	name = name.lower()
	if(name == "battleaxe"):
		return Weapon("battleaxe", "martial melee", 10, "gp", "1d8",
				"slashing", 4, "versatile (1d10)")
	elif(name == "flail"):
		return Weapon("flail", "martial melee", 10, "gp", "1d8",
				"bludgeoning", 2, "null")
	elif(name == "glaive"):
		return Weapon("glaive", "martial melee", 20, "gp", "1d10",
				"slashing", 6, "heavy reach two-handed")
	elif(name == "greataxe"):
		return Weapon("greataxe", "martial melee", 30, "gp", "1d12",
				"slashing", 7, "heavy two-handed")
	elif(name == "greatsword"):
		return Weapon("greatsword", "martial melee", 50, "gp", "2d6",
				"slashing", 6, "heavy two-handed")
	elif(name == "halberd"):
		return Weapon("halberd", "martial melee", 20, "gp", "1d10",
				"slashing", 6, "heavy reach two-handed")
	elif(name == "lance"):
		return Weapon("lance", "martial melee", 10, "gp", "1d12",
				"piercing", 6, "reach special")
	elif(name == "longsword"):
		return Weapon("longsword", "martial melee", 15, "gp", "1d8",
				"slashing", 3, "versatile (1d10)")
	elif(name == "maul"):
		return Weapon("maul", "martial melee", 10, "gp", "2d6",
				"bludgeoning", 10, "heavy two-handed")
	elif(name == "morningstar"):
		return Weapon("morningstar", "martial melee", 15, "gp",
				"1d8", "piercing", 4, "null")
	elif(name == "pike"):
		return Weapon("pike", "martial melee", 5, "gp", "1d10",
				"piercing", 18, "heavy reach two-handed")
	elif(name == "rapier"):
		return Weapon("rapier", "martial melee", 25, "gp", "1d8",
				"piercing", 2, "finesse")
	elif(name == "scimitar"):
		return Weapon("scimitar", "martial melee", 25, "gp", "1d6",
				"slashing", 3, "finesse light")
	elif(name == "shortsword"):
		return Weapon("shortsword", "martial melee", 10, "gp", "1d6",
				"piercing", 2, "finesse light")
	elif(name == "trident"):
		return Weapon("trident", "martial melee", 5, "gp", "1d6",
				"piercing", 4, "thrown (range 20/60) versatile (1d8)")
	elif(name == "war pick"):
		return Weapon("war pick", "martial melee", 5, "gp", "1d8",
				"piercing", 2, "null")
	elif(name == "warhammer"):
		return Weapon("warhammer", "martial melee", 15, "gp", "1d8",
				"bludgeoning", 2, "versatile (1d10)")
	elif(name == "whip"):
		return Weapon("whip", "martial melee", 2, "gp", "1d4",
				"slashing", 3, "finesse reach")



def getMartialRangedByName(name: str = "blowgun") -> Weapon:
	name = name.lower()
	if(name == "blowgun"):
		return Weapon("blowgun", "martial ranged", 10, "gp", "1",
				"piercing", 1, "ammunition (range 25/100) loading")
	elif(name == "hand crossbow"):
		return Weapon("hand crossbow", "martial ranged", 75, "gp",
				"1d6", "piercing", 3,
				"ammunition (range 30/120) light loading")
	elif(name == "heavy crossbow"):
		return Weapon("heavy crossbow", "martial ranged", 50, "gp",
				"1d10", "piercing", 18,
				"ammunition (range 100/400) heavy loading two-handed")
	elif(name == "longbow"):
		return Weapon("longbow", "martial ranged", 50, "gp", "1d8",
				"piercing", 2,
				"ammunition (range 150/600) heavy two-handed")
	elif(name == "net"):
		return Weapon("net", "martial ranged", 1, "gp", 0, "null", 3,
				"special thrown (range 5/15)")


# //---------// //---------// //---------//
# Main function statements
# //---------// //---------// //---------//
