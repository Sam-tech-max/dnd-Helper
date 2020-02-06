class Stat:
	def __init__(self, name="strength",  score=10, hasProficiency=False,
	mod=0):
		self.name = name
		self.hasProficiency = hasProficiency
		self.score = score
		self.mod = mod
		
	def printStat(self):
		print("Stat Name: ", self.getName())
		if(self.getHasProficiency()):
			print("You are proficient in ", self.getName())
		if(self.getScore() > 0):
			print("Score: ",str(self.getScore()))
		print("Modifier: ", self.getMod())
		
# //---------// //---------// //---------//
# These are the get and set methods for the
# stat class
# //---------// //---------// //---------//
		
	def getHasProficiency(self):
		return self.hasProficiency
		
	def setHasProficiency(self, hasProficiency):
		self.hasProficiency = hasProficiency
		
	def getMod(self):
		return self.mod
		
	def setMod(self, mod):
		self.mod = mod
		
	def getName(self):
		return self.name
		
	def setName(self, name):
		self.name = name
		
	def getScore(self):
		return self.score
		
	def setScore(self, score):
		self.score = score


class Stats:
	def __init__(self, proficienyBonus=0, strength=15, dexterity=14,
	constitution=13, intelligence=12, wisdom=10, charisma=8):
		self.stats = list()
		# Strength
		self.stats.append(Stat("strength", strength))
		self.stats.append(Stat("strength: saving throws", 0))
		self.stats.append(Stat("strength: atheletics", 0))
		# Dexterity
		self.stats.append(Stat("dexterity", dexterity))
		self.stats.append(Stat("dexterity: saving throws", 0))
		self.stats.append(Stat("dexterity: acrobatics", 0))
		self.stats.append(Stat("dexterity: sleight of hand", 0))
		self.stats.append(Stat("dexterity: stealth", 0))
		# Constitution
		self.stats.append(Stat("constitution", constitution))
		self.stats.append(Stat("constitution: saving throws", 0))
		# Intelligence
		self.stats.append(Stat("intelligence", intelligence))
		self.stats.append(Stat("intelligence: saving throws", 0))
		self.stats.append(Stat("intelligence: arcana", 0))
		self.stats.append(Stat("intelligence: history", 0))
		self.stats.append(Stat("intelligence: investigation", 0))
		self.stats.append(Stat("intelligence: nature", 0))
		self.stats.append(Stat("intelligence: religion", 0))
		# Wisdom
		self.stats.append(Stat("wisdom", wisdom))
		self.stats.append(Stat("wisdom: saving throws", 0))
		self.stats.append(Stat("wisdom: animal handling", 0))
		self.stats.append(Stat("wisdom: insight", 0))
		self.stats.append(Stat("wisdom: medicine", 0))
		self.stats.append(Stat("wisdom: perception", 0))
		self.stats.append(Stat("wisdom: survival", 0))
		# Charisma
		self.stats.append(Stat("charisma", charisma))
		self.stats.append(Stat("charisma: saving throws", 0))
		self.stats.append(Stat("charisma: deception", 0))
		self.stats.append(Stat("charisma: intimidation", 0))
		self.stats.append(Stat("charisma: performance", 0))
		self.stats.append(Stat("charisma: persuasion", 0))
		
		self.proficienyBonus = proficienyBonus
		
# //---------// //---------// //---------//
# These are the get and set methods
# //---------// //---------// //---------//
	def getStat(self, name):
		self.calculateMods()
		for stat in self.stats:
			if(stat.getName() == name):
				return stat
		return Stat()
		
	def setStat(self, stat):
		name = stat.getName()
		for each in self.stats:
			if(name == each.getName()):
				each.setScore(stat.getScore())
				each.setMod(stat.getMod())
				each.setHasProficiency(stat.getHasProficiency())
		self.calculateMods()

# //---------// //---------// //---------//
# These are the other functions associtated
# with the Stats class
# //---------// //---------// //---------//
		
	def printStats(self):
		self.calculateMods()
		print("The Stats for your Character are:")
		print("Proficiency Bonus: " + str(self.proficienyBonus))
		for stat in self.stats:
			stat.printStat()
			
	def calculateMod(self, score):
		if(score == 1):
			return -5
		elif(score == 2 or score == 3):
			return -4
		elif(score == 4 or score == 5):
			return -3
		elif(score == 6 or score == 7):
			return -2
		elif(score == 8 or score == 9):
			return -1
		elif(score == 10 or score == 11):
			return 0
		elif(score == 12 or score == 13):
			return 1
		elif(score == 14 or score == 15):
			return 2
		elif(score == 16 or score == 17):
			return 3
		elif(score == 18 or score == 19):
			return 4
		elif(score == 20 or score == 21):
			return 5
		elif(score == 22 or score == 23):
			return 6
		elif(score == 24 or score == 25):
			return 7
		elif(score == 26 or score == 27):
			return 8
		elif(score == 28 or score == 29):
			return 9
		elif(score == 30):
			return 10
		else:
			return score
			
	def calculateMods(self):
		currentMod = 0
		for stat in self.stats:
			if(":" in stat.getName()):
				if(stat.getHasProficiency()):
					stat.setMod(currentMod + self.proficienyBonus)
				else:
					stat.setMod(currentMod)
			else: 
				currentMod = self.calculateMod(stat.getScore())
				stat.setMod(currentMod)
