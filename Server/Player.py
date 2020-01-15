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
	alignment="true neutral", experiencePoints=0, proficiencyBonus=0,
	inspiration=0, armorClass=0, initiative=0, speed=0, hitPoints=0,
	hitDie="1d6", age=20, strength=15, dexterity=14, constitution=13,
	intelligence=12, wisdom=10, charisma=8):
		# String Types
		self.alignment = alignment
		self.background = background
		self.characterName = characterName
		self.classRole = classRole
		self.hitDie = hitDie
		self.playerName = playerName
		self.race = race
		# Integer Types
		self.age = age
		self.armorClass = armorClass
		self.experiencePoints = experiencePoints
		self.hitPoints = hitPoints
		self.inspiration = inspiration
		self.initiative = initiative
		self.level = level
		self.proficiencyBonus = proficiencyBonus
		self.speed = speed
		# Stats type: Strength, Dexiterity, Consititution, Intelligence,
		# Wisdom, Charisma, and Proficiency Bonus are within this class. 
		self.stats = Stats.Stats(proficiencyBonus, strength, dexterity,
		constitution, intelligence, wisdom, charisma)
		# updates the modifiers
		self.stats.calculateMods()
	
	#Stuff to do:
	# armorClass, initiative, speed, hitpoints, hitDie
	def printPlayer(self, withStats=True):
		print("//----------// Character Attributes //----------//")
		print("Character Name: " + self.characterName)
		print("Class: " + self.classRole)
		print("Level: " + str(self.level))
		print("Background: " + self.background)
		print("Player Name: " + self.playerName)
		print("Race: " + self.race)
		print("Alignment: " + self.alignment)
		print("Experience Points: " + str(self.experiencePoints))
		print("Proficiency Bonus: " + str(self.proficiencyBonus))
		print("Inspiration: " + str(self.inspiration))
		print("Armor Class: " + str(self.armorClass))
		print("Initiative: " + str(self.initiative))
		print("Speed: " + str(self.speed))
		print("Hit Points: " + str(self.hitPoints))
		print("Hit Die: " + self.hitDie)
		print("Age: " + str(self.age))
		if(withStats):
			self.stats.printStats()
		print("//----------// //----------// //----------//")
		
# //---------// //---------// //---------//
# These are the get and set methods
# //---------// //---------// //---------//
	#Stuff to do:
	# experiencePoints, proficiencyBounus, inspiration, armorClass, initiative, speed, hitpoints, hitDie
	def getAge(self):
		return self.age

	def setAge(self, age):
		if('int' in str(type(age))):
			self.age = age
		else:
			print("Error :: incorrect type value :: need int")
		
	def getAlignment(self):
		return self.alignment
	
	def setAlignment(self, alignment):
		self.alignment = alignment
		
	def getBackground(self):
		return self.background
		
	def setBackground(self, background):
		self.background = background
		
	def getCharacterName(self):
		return self.characterName
		
	def setCharacterName(self, characterName):
		self.characterName = characterName

	def getClassRole(self):
		return self.classRole
		
	def setClassRole(self, classRole):
		return self.classRole

	# Inspiration

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

	def getRace(self):
		return self.race
		
	def setRace(self, race):
		self.race = race
		
	def getStats(self):
		return self.stats
		
	def setStats(self, stats):
		self.stats = stats
		
	def getSpeed(self):
		return self.speed
		
	def setSpeed(self, speed):
		self.speed = speed
		
# //---------// //---------// //---------//
# Other function statements with player class
# //---------// //---------// //---------//
	def convertToJSON(self):
		temp = json.dumps(self.__dict__)
		return temp

# //---------// //---------// //---------//
# Main function statements
# //---------// //---------// //---------//
