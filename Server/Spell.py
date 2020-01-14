
class Spell:
# //---------// //---------// //---------//
# Init statement: makes a spell
# If you don't put anything in the init statement,
# then the spell will be Acid Splash 
# //---------// //---------// //---------//
	def __init__(self, level=0, name="Acid Splash",
	castingTime="1 Action", duration="Instantaneous", rangeArea="60 ft",
	school="Conjuration", attackSave="DEX Save", components="V,S",
	damageEffect="Acid", description="You hurl a bubble of acid. Choose one or two creatures you can see within range. If you choose two, they must be within 5 feet of each other. A target must succeed on a Dexterity saving throw or take 1d6 acid damage. This spell’s damage increases by 1d6 when you reach 5th level (2d6), 11th level (3d6), and 17th level (4d6)."):
			self.level = level
			self.name = name
			self.castingTime = castingTime
			self.duration = duration
			self.rangeArea = rangeArea
			self.school = school
			self.attackSave = attackSave
			self.components = components
			self.damageEffect = damageEffect
			self.description = description
			
	def printSpell(self):
		print("//----------// " + self.getName() + " //----------//" )
		print("Level: " + str(self.getLevel()))
		print("Name: " + self.getName())
		print("Casting Time: " + self.getCastingTime())
		print("Duration: " + self.getDuration())
		print("Range/Area: " + self.getRangeArea())
		print("School: " + self.getSchool())
		print("Attack/Save: " + self.getAttackSave())
		print("Components: " + self.getComponents())
		print("Damage/Effect: " + self.getDamageEffect())
		print("Description: " + self.getDescription())
		print("//----------// //----------// //----------//")
# //---------// //---------// //---------//
# get and set functions
# //---------// //---------// //---------//

	def getAttackSave(self):
		return self.attackSave
		
	def setAttackSave(self, attackSave):
		self.attackSave = attackSave
		
	def getCastingTime(self):
		return self.castingTime
		
	def setCastingTime(self, castingTime):
		self.castingTime = castingTime
		
	def getComponents(self):
		return self.components
		
	def setComponents(self, components):
		self.components = components
		
	def getDamageEffect(self):
		return self.damageEffect
		
	def setDamageEffect(self, damageEffect):
		self.damageEffect = damageEffect
		
	def getDescription(self):
		return self.description
		
	def setDescription(self, description):
		self.description = description
		
	def getDuration(self):
		return self.duration
		
	def setDuration(self, duration):
		self.duration = duration
		
	def getLevel(self):
		return self.level
		
	def setLevel(self, level):
		if('int' in str(type(level))):
			if(level < 0):
				print("Spell level too low")
			elif(level > 9):
				print("Spell level too high")
			else:
				self.level = level
		else:
			print("Error :: incorrect type value :: need int")
	
	def getName(self):
		return self.name
		
	def setName(self, name):
		self.name = name
	
	def getRangeArea(self):
		return self.rangeArea
		
	def setRangeArea(self, rangeArea):
		self.rangeArea = rangeArea
	
	def getSchool(self):
		return self.school
	
	def setSchool(self, school):
		self.school = school
