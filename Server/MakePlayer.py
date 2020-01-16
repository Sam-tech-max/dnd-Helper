import Player
class MakePlayer:
	def __init__(self):
		self.player = Player.Player()

# //---------// //---------// //---------//
# Choose function statements
# //---------// //---------// //---------//		
	def chooseAge(self, ageDescription):
		age = input(ageDescription)
		self.getPlayer().setAge(int(age))
		
	def chooseAlignment(self, alignmentDescription):
		# Chaotic, neutral or lawful
		print("Alignment Description:", alignmentDescription)
		cnl = str(input("Choose chaotic, neutral or lawful: ")).lower()
		if(cnl == "chaotic" or cnl == "neutral" or cnl == "lawful"):
			# evil, neutral or good
			eng = input("Choose evil, neutral or good: ").lower()
			if(eng == "evil" or eng == "neutral" or eng == "good"):
				self.getPlayer().setAlignment(cnl + " " + eng)
			else:
				self.chooseAlignment(alignmentDescription)
		else:
			self.chooseAlignment(alignmentDescription)
			
	def chooseCharacterName(self, nameDescription, lastNames):
		print("These are the common first names of this race and gender:", nameDescription)
		print("These are the common last names of this race and gender:", lastNames)
		name = input()
		self.getPlayer().setCharacterName(name)
			
	def chooseDwarf(self):
		print("You Choose Dwarf")
		player = self.getPlayer()
		if(player.getGender() == "male"):
			self.chooseCharacterName("Adrik, Alberich, Baern, Barendd, Brottor, Bruenor, Dain, Darrak, Delg, Eberk, Einkil, Fargrim, Flint, Gardain, Harbek, Kildrak, Morgran, Orsik, Oskar, Rangrim, Rurik, Taklinn, Thoradin, Thorin, Tordek, Traubon, Travok, Ulfgar, Veit, Vondal","Balderk, Battlehammer, Brawnanvil, Dankil, Fireforge, Frostbeard, Gorunn, Holderhek, Ironfist, Loderr, Lutgehr, Rumnaheim, Strakeln, Torunn, Ungart")
		elif(player.getGender() == "female"):
			self.chooseCharacterName("Amber, Artin, Audhild, Bardryn, Dagnal, Diesa, Eldeth, Falkrunn, Finellen, Gunnloda, Gurdis, Helja, Hlin, Kathra, Kristryd, Ilde, Liftrasa, Mardred, Riswynn, Sannl, Torbera, Torgga, Vistra","Balderk, Battlehammer, Brawnanvil, Dankil, Fireforge, Frostbeard, Gorunn, Holderhek, Ironfist, Loderr, Lutgehr, Rumnaheim, Strakeln, Torunn, Ungart")
		player.setRace("dwarf")
		constitution = player.getStat("constitution")
		constitution.setScore(constitution.getScore() + 2)
		self.chooseAge("What is the age of your Dwarf? Dwarves mature at the same rate as humans, but they're considered young until they reach the age of 50. On average, they live about 350 years.")
		self.chooseAlignment("Most dwarves are lawful, believing firmly in the benefits of a well-ordered society. They tend toward good as well, with a strong sense of fair play and a belief that everyone deserves to share in the benefits of a just order.")
		self.chooseHieghtAndWeight("Dwarves stand between 4 and 5 feet tall and average about 150 pounds.")
		player.setSpeed(25)
		player.setDarkvision(60)
		player.addProficiency("battleaxe")
		player.addProficiency("handaxe")
		player.addProficiency("throwing hammer")
		player.addProficiency("warhammer")
		player.addProficiency("intelligence: history: origin of stonework: add double your proficiency bonus to the check")
		player.addProficiency("common")
		player.addProficiency("dwarvish")
		subrace = ""
		while(subrace != "hill" and subrace != "mountain"):
			print("Choose between the Dwarven subraces: Hill or Mountain Dwarves")
			subrace = str(input()).lower()
		player.setSubrace(subrace)
		if(player.getSubrace() == "hill"):
			wisdom = player.getStats().getStat("wisdom")
			wisdom.setScore(wisdom.getScore() + 1)
			player.setStat(wisdom)
			player.setHitPoints(player.getHitPoints() + 1)
		elif(player.getSubrace() == "mountain"):
			strength = player.getStat("strength")
			strength.setScore(strength.getScore() + 2)
			player.addProficiency("light armor")
			player.addProficiency("medium armor")
			
	def chooseElf(self):
		print("You Choose Elf")
	
	def chooseGender(self):
		gender = input("Do you want your character to be male or female? ")
		gender.lower()
		if(gender == "male"):
			self.getPlayer().setGender(gender)
		elif(gender == "female"):
			self.getPlayer().setGender(gender)
		else:
			print("Not a valid gender")
			self.chooseGender()
		
	def chooseHieghtAndWeight(self, hieghtAndWeightDescription):
		print("Height and Weight Description:", hieghtAndWeightDescription)
		height = int(input("Please enter a height in inches: "))
		weight = int(input("Please enter a weight in pounds: "))
		self.getPlayer().setHeight(height)
		self.getPlayer().setWeight(weight)
		

	def choosePlayerName(self):
		name = input("Please enter your name: ")
		self.getPlayer().setPlayerName(name)
		
	def chooseRace(self):
		print("Choose your race: ")
		print("Enter 1 for Dwarf")
		print("Enter 2 for Elf")
		race = input()
		if(race == "1"):
			self.chooseDwarf()
		elif(race == "2"):
			self.chooseElf()
		else:
			print("You did not choose a correct race")
			self.chooseRace()

	def chooseStats(self):
		print("AutoRoll?: Y/N")
		autoRoll = input()
		if(autoRoll == "Y"):
			print("Yes to autoRoll")
		elif(autoRoll == "N"):
			print("Enter in rolls:")
			stats = self.getPlayer().getStats()
			strength = int(input("Str: "))
			stats.getStat("strength").setScore(strength)
			dexterity = int(input("Dex: "))
			stats.getStat("dexterity").setScore(dexterity)
			constitution = int(input("Con: "))
			stats.getStat("constitution").setScore(constitution)
			intelligence = int(input("Int: "))
			stats.getStat("intelligence").setScore(intelligence)
			wisdom = int(input("Wis: "))
			stats.getStat("wisdom").setScore(wisdom)
			charisma = int(input("Cha: "))
			stats.getStat("charisma").setScore(charisma)
		else:
			print("Wrong input")
			self.rolls()
		
	def newPlayer(self):
		#self.choosePlayerName()
		#self.chooseStats()
		self.chooseGender()
		self.chooseRace()


# //---------// //---------// //---------//
# Set and Get function statements
# //---------// //---------// //---------//
	def getPlayer(self):
		return self.player
		
	def setPlayer(self, player):
		self.player = player


# //---------// //---------// //---------//
# Main function statements
# //---------// //---------// //---------//
playerMaker = MakePlayer()
playerMaker.player.printPlayer(False)
playerMaker.newPlayer()
playerMaker.player.printPlayer(False)
