import Player

class Barbarian(Player.Player):
	def __init__(self, characterName="John Doe",
	level=1, background="Hermit", playerName="Odin", race="Elf",
	alignment="true neutral", experiencePoints=0,
	inspiration=0, armorClass=0, initiative=0, speed=0, hitPoints=0,
	age=20, strength=15, dexterity=14, constitution=13,
	intelligence=12, wisdom=10, charisma=8):
		# The proficiency bonus is from page 41(PDF) 47 Physical of the
		# player's handbook.
		proficiencyBonus = 2
		rage = 2
		if(level <= 0):
			print("level error::level needs to be more than 0")
			print("Changing level to 1")
			level = 1
			
			
			proficiencyBonus = 2
		elif (level <= 4):
			proficiencyBonus = 2
			rage = 2
		elif (level <=8):
			proficiencyBonus = 3
			rage = 2
		elif (level <= 12):
			proficiencyBonus = 4
			rage = 3
		elif (level <= 15):
			proficiencyBonus = 5
			rage = 3
		elif (level <= 16):
			proficiencyBonus = 5
			rage = 4
		elif (level <= 20):
			proficiencyBonus = 6
			rage = 4
		else:
			print("level error::level needs to be less than 21")
			print("Changing level to 20")
			level = 20
			proficiencyBonus = 6
		
			
			
		super().__init__(characterName, "barbarian", level, background,
		playerName, race, alignment, experiencePoints, proficiencyBonus, 
		inspiration, armorClass, initiative, speed, hitPoints, "1d12",
		age, strength, dexterity, constitution, intelligence, wisdom,
		charisma)
		# Adds the proficiencies for strength and :
		stat = self.stats.getStat("strength: saving throws")
		stat.setHasProficiency(True)
		self.stats.setStat(stat)

		stat = self.stats.getStat("constitution: saving throws")
		stat.setHasProficiency(True)
		self.stats.setStat(stat)
		
		
		# updates the stat modifiers
		self.stats.calculateMods()
		
		# gets the constitution modifier
		conMod = self.stats.getStat("constitution").getMod()
		hitPoints = 12 + conMod
		
		# The loop which updates the stats when the levels are greater
		# than 1
		while(level > 1):
			hitPoints += 7 + conMod
			level -= 1
		self.hitPoints = hitPoints
		
# //---------// //---------// //---------//
# Main function statements
# //---------// //---------// //---------//			
barbarian = Barbarian("Derick", 6, "Hermin", "Samuel Collins", "Human",
"chaotic neutral", 0, 0, 0, 0, 0, 0, 30, 15, 14, 13, 12, 10, 8)
barbarian.printPlayer()
