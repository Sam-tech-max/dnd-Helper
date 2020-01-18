import json
import Stats
# This class is to keep track of your dnd chacter.
# It is based off of the 5e dnd Character Sheet

class Player:
# //---------// //---------// //---------//
# Init statement: sets your player as a gengeric character
# If you don't put anything in the init statement,
# then the values below will be what the character will be.
# //---------// //---------// //---------//

	def __init__(self, characterName="John Doe", classRole="fighter",
	level=1, background="Hermit", playerName="Odin", race="Elf",
	subrace="Wood",	alignment="true neutral", experiencePoints=0,
	proficiencyBonus=0,	inspiration=0, armorClass=0, initiative=0,
	speed=0, hitPoints=0, hitDie="1d6", age=20, height=68, weight=150,
	darkvision=0, size="medium", gender="male", strength=15,
	dexterity=14, constitution=13, intelligence=12, wisdom=10,
	charisma=8):
		# String Types
		self.alignment = alignment
		self.background = background
		self.characterName = characterName
		self.classRole = classRole
		self.hitDie = hitDie
		self.playerName = playerName
		self.race = race
		self.subrace = subrace
		self.gender = gender
		# Integer Types
		self.age = age
		self.armorClass = armorClass
		self.darkvision = darkvision
		self.experiencePoints = experiencePoints
		self.height = height
		self.hitPoints = hitPoints
		self.inspiration = inspiration
		self.initiative = initiative
		self.level = level
		self.proficiencyBonus = proficiencyBonus
		self.size = size
		self.speed = speed
		self.weight = weight
		# Stats type: Strength, Dexiterity, Consititution, Intelligence,
		# Wisdom, Charisma, and Proficiency Bonus are within this class. 
		self.stats = Stats.Stats(proficiencyBonus, strength, dexterity,
		constitution, intelligence, wisdom, charisma)
		# updates the modifiers
		self.stats.calculateMods()
		# string arrary for proficiencies and languages
		self.proficiencies = list()
		# Features and Traits
		self.features = list()
	
	#Stuff to do:
	# armorClass, initiative, speed, hitpoints, hitDie
	def printPlayer(self, withStats=True):
		print("//----------// Character Attributes //----------//")
		print("Character Name:", self.getCharacterName())
		print("Class:", self.getClassRole())
		print("Level:", self.getLevel())
		print("Background:", self.getBackground())
		print("Player Name:", self.getPlayerName())
		print("Race:", self.getSubrace(),self.getRace())
		print("Alignment:", self.getAlignment())
		print("Experience Points:", self.getExperiencePoints())
		print("Proficiency Bonus:", self.getProficiencyBonus())
		print("Inspiration:", self.getInspiration())
		print("Armor Class:", self.getArmorClass())
		print("Initiative:", self.getInitiative())
		print("Speed:", self.getSpeed())
		print("Darkvision:", self.getDarkvision(), "ft")
		print("Hit Points:", self.getHitPoints())
		print("Hit Die:", self.getHitDie())
		print("Age:", self.getAge())
		print("Height:", self.getHeight(), "in")
		print("Weight:", self.getWeight(), "lb")
		print("Size:", self.getSize())
		self.printProficiencies()
		self.printFeatures()
		if(withStats):
			self.getStats().printStats()
		print("//----------// //----------// //----------//")
		
	def printFeatures(self):
		if(len(self.getFeatures()) > 0):
			print("//----------// //----------//")
			fea = ""
			for each in self.getFeatures():
				fea += each + ", "
			print("Your Features and Traits are:", fea)
		
	def printProficiencies(self):
		if(len(self.getProficiencies()) > 0):
			print("//----------// //----------//")
			pro = ""
			for each in self.getProficiencies():
				pro += each + ", "
			print("You Have Proficiencies in:", pro)
# //---------// //---------// //---------//
# These are the get and set methods
# //---------// //---------// //---------//
	#Stuff to do:
	#initiative, speed, hitpoints, hitDie
	def getAge(self) -> int:
		return self.age

	def setAge(self, age:int):
		self.age = age
				
	def getAlignment(self) -> str:
		return self.alignment
	
	def setAlignment(self, alignment: str):
		self.alignment = alignment
		
	def getArmorClass(self) -> int:
		return self.armorClass
		
	def setArmorClass(self,armorClass: int):
		self.armorClass = armorClass
		
	def getBackground(self) -> str:
		return self.background
		
	def setBackground(self, background: str):
		self.background = background
		
	def getCharacterName(self) -> str:
		return self.characterName
		
	def setCharacterName(self, characterName: str):
		self.characterName = characterName

	def getClassRole(self) -> str:
		return self.classRole
		
	def setClassRole(self, classRole: str):
		self.classRole = classRole
		
	def getDarkvision(self):
		return self.darkvision
		
	def setDarkvision(self, darkvision):
		self.darkvision = darkvision
		
	def getExperiencePoints(self):
		return self.experiencePoints
		
	def setExperiencePoints(self, experiencePoints):
		self.experiencePoints = experiencePoints
		
	def getFeatures(self):
		return self.features
		
	def setFeatures(self, features):
		self.features = features
		
	def addFeatures(self, featureName):
		features = self.getFeatures()
		features.append(featureName)
		self.setFeatures(features)
		
	def getGender(self):
		return self.gender
		
	def setGender(self, gender):
		self.gender = gender
		
	def getHeight(self):
		return self.height
		
	def setHeight(self, height):
		self.height = height
		
	def getHitDie(self):
		return self.hitDie
		
	def setHitDie(self, hitDie):
		self.hitDie = hitDie
		
	def getHitPoints(self):
		return self.hitPoints
		
	def setHitPoints(self, hitPoints):
		self.hitPoints = hitPoints
		
	def getInitiative(self):
		return self.initiative
		
	def setInitiative(self, initiative):
		self.initiative = initiative

	def getInspiration(self):
		return self.inspiration
		
	def setInspiration(self, inspiration):
		self.inspiration = inspiration

	def getLevel(self):
		return self.level
		
	def setLevel(self, level):
		if('int' in str(type(level))):
			self.level = level
		else:
			print("Error :: incorrect type value :: need int")

	def getPlayerName(self):
		return self.playerName
	
	def setPlayerName(self, playerName):
		self.playerName = playerName
		
	def getProficiencies(self):
		return self.proficiencies
		
	def setProficiencies(self,proficiencies):
		self.proficiencies = proficiencies
		
	def isProficiency(self, proficiencyName):
		for each in self.getProficiencies():
			if(each == proficiencyName):
				return True
		return False
		
	def addProficiency(self, proficiencyName):
		if(not self.isProficiency(proficiencyName)):
			proficiencies = self.getProficiencies()
			proficiencies.append(str(proficiencyName))
			self.setProficiencies(proficiencies)
		
	def getProficiencyBonus(self):
		return self.proficiencyBonus
		
	def setProficiencyBonus(self, proficiencyBonus):
		self.proficiencyBonus = proficiencyBonus

	def getRace(self):
		return self.race
		
	def setRace(self, race):
		self.race = race
		
	def getSize(self):
		return self.size
		
	def setSize(self, size):
		self.size = size
			
	def getSpeed(self):
		return self.speed
		
	def setSpeed(self, speed):
		self.speed = speed
			
	def getStats(self):
		return self.stats
		
	def setStats(self, stats):
		self.stats = stats
		
	def getStat(self, name):
		return self.stats.getStat(name)
		
	def setStat(self, stat):
		self.stats.setStat(stat)
		
	def getSubrace(self):
		return self.subrace
		
	def setSubrace(self, subrace):
		self.subrace = subrace

	def getWeight(self):
		return self.weight
		
	def setWeight(self, weight):
		self.weight = weight
		
# //---------// //---------// //---------//
# Other function statements with player class
# //---------// //---------// //---------//
	def convertToJSON(self):
		temp = json.dumps(self.__dict__)
		return temp

# //---------// //---------// //---------//
# Main function statements
# //---------// //---------// //---------//
#player = Player()
#player.printPlayer(False)
