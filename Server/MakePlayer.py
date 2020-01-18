import Player
class MakePlayer:
	def __init__(self):
		self.player = Player.Player()

# //---------// //---------// //---------//
# Choose function statements
# //---------// //---------// //---------//		
	def chooseAge(self, ageDescription):
		print("//----------// //----------// //----------// //----------//")
		age = input(ageDescription)
		self.getPlayer().setAge(int(age))
		print("//----------// //----------// //----------// //----------//")
		
	def chooseAlignment(self, alignmentDescription):
		# Chaotic, neutral or lawful
		print("//----------// //----------// //----------// //----------//")
		print("Alignment Description:", alignmentDescription)
		cnl = str(input("Choose chaotic, neutral or lawful: ")).lower()
		if(cnl == "chaotic" or cnl == "neutral" or cnl == "lawful"):
			# evil, neutral or good
			eng = input("Choose evil, neutral or good: ").lower()
			if(eng == "evil" or eng == "neutral" or eng == "good"):
				self.getPlayer().setAlignment(cnl + " " + eng)
				print("//----------// //----------// //----------// //----------//")
			else:
				self.chooseAlignment(alignmentDescription)
		else:
			self.chooseAlignment(alignmentDescription)
			
	def chooseCharacterName(self, nameDescription, lastNames):
		print("//----------// //----------// //----------// //----------//")
		print("These are the common first names of this race and gender:", nameDescription)
		print("These are the common last names of this race and gender:", lastNames)
		name = input()
		self.getPlayer().setCharacterName(name)
		print("//----------// //----------// //----------// //----------//")
			
	def chooseDwarf(self):
		print("//----------// //----------// //----------// //----------//")
		print("You Choose Dwarf")
		player = self.getPlayer()
		if(player.getGender() == "male"):
			self.chooseCharacterName("Adrik, Alberich, Baern, Barendd, Brottor, Bruenor, Dain, Darrak, Delg, Eberk, Einkil, Fargrim, Flint, Gardain, Harbek, Kildrak, Morgran, Orsik, Oskar, Rangrim, Rurik, Taklinn, Thoradin, Thorin, Tordek, Traubon, Travok, Ulfgar, Veit, Vondal","Balderk, Battlehammer, Brawnanvil, Dankil, Fireforge, Frostbeard, Gorunn, Holderhek, Ironfist, Loderr, Lutgehr, Rumnaheim, Strakeln, Torunn, Ungart")
		elif(player.getGender() == "female"):
			self.chooseCharacterName("Amber, Artin, Audhild, Bardryn, Dagnal, Diesa, Eldeth, Falkrunn, Finellen, Gunnloda, Gurdis, Helja, Hlin, Kathra, Kristryd, Ilde, Liftrasa, Mardred, Riswynn, Sannl, Torbera, Torgga, Vistra","Balderk, Battlehammer, Brawnanvil, Dankil, Fireforge, Frostbeard, Gorunn, Holderhek, Ironfist, Loderr, Lutgehr, Rumnaheim, Strakeln, Torunn, Ungart")
		player.setRace("dwarf")
		constitution = player.getStat("constitution")
		constitution.setScore(constitution.getScore() + 2)
		player.setStat(constitution)
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
		self.setPlayer(player)
		print("//----------// //----------// //----------// //----------//")
			
	def chooseElf(self):
		print("//----------// //----------// //----------// //----------//")
		print("You Choose Elf")
		player = self.getPlayer()
		# Elven names, I didn't use child names yet.
		lastNames = " Amakiir (Gemflower), Am astacia (Starflower), Galanodel (M oonwhisper), H olim ion (Diam onddew), Ilphelkiir (Gem blossom ), Liadon (Silverfrond), M eliamne (Oakenheel), Nai'lo (Nightbreeze), Siannodel (M oonbrook), Xiloscient (Goldpetal)"
		if(player.getGender() == "male"):
			self.chooseCharacterName(" Adran, Aelar, Aramil, Arannis, Aust, Beiro, Berrian, Carric , Enialis, Erdan, Erevan, Galinndan, Hadarai, Heian, Himo, Immeral, Ivellios, Laucian, Mindartis, Paelias, Peren, Quarion, Riardon, Rolen, Soveliss, Thamior, Tharivol, Theren, Varis", lastNames)
		elif(player.getGender() == "female"):
			self.chooseCharacterName("Adrie, Althaea, Anastrianna, Andraste, Antinua, Bethrynna, Birel, Caelynn, Drusilia, Enna, Felosial, Ielenia, Jelenneth, Keyleth, Leshanna, Lia, Meriele, M ialee, Naivara, Quelenna, Quillathe, Sariel, Shanairra, Shava, Silaqui, Theirastra, Thia, Vadania, Valanthe, Xanaphia", lastNames)
		player.setRace("elf")
		# all elves get a plus two to the dexterity score
		dexterity =  player.getStat("dexterity")
		dexterity.setScore(dexterity.getScore() + 2)
		player.setStat(dexterity)
		# age, alignment and size
		self.chooseAge("Although elves reach physical maturity at about the same age as humans, the elven understanding of adulthood goes beyond physical growth to encompass worldly experience. An elf typically claims adulthood and an adult name around the age of 100 and can live to be 750 years old.")
		self.chooseAlignment("Elves love freedom , variety, and selfexpression, so they lean strongly toward the gentler aspects of chaos. They value and protect others' freedom as well as their own, and they are more often good than not. The drow are an exception; their exile into the Underdark has made them vicious and dangerous. D row are m ore often evil than not.")
		self.chooseHieghtAndWeight("Elves range from under 5 to over 6 feet tall and have slender builds.")
		# speed of most elves is 30, size is medium, darkvision is 60 ft
		player.setSpeed(30)
		player.setSize("medium")
		player.setDarkvision("60")
		# Keen Senses, Fey Ancestry, Trance
		perception = player.getStat("wisdom: perception")
		perception.setHasProficiency(True)
		player.setStat(perception)
		player.addProficiency("saving throws: charmed: advantage")
		player.addFeatures("magic can't put you to sleeps")
		player.addFeatures("Elvels don't need to sleep. Instead, they meditate deeply, remaining semiconscious, for 4 hours a day")
		# Languages that elves speak are common and elvish
		player.addProficiency("common")
		player.addProficiency("elvish")
		
		# last thing in Choose Elf
		self.setPlayer(player)
		print("//----------// //----------// //----------// //----------//")
	
	def chooseGender(self):
		print("//----------// //----------// //----------// //----------//")
		gender = input("Do you want your character to be male or female? ")
		gender.lower()
		if(gender == "male"):
			self.getPlayer().setGender(gender)
		elif(gender == "female"):
			self.getPlayer().setGender(gender)
		else:
			print("Not a valid gender")
			self.chooseGender()
		print("//----------// //----------// //----------// //----------//")
		
	def chooseHieghtAndWeight(self, hieghtAndWeightDescription):
		print("//----------// //----------// //----------// //----------//")
		print("Height and Weight Description:", hieghtAndWeightDescription)
		height = int(input("Please enter a height in inches: "))
		weight = int(input("Please enter a weight in pounds: "))
		self.getPlayer().setHeight(height)
		self.getPlayer().setWeight(weight)
		print("//----------// //----------// //----------// //----------//")

	def choosePlayerName(self):
		name = input("Please enter your name: ")
		self.getPlayer().setPlayerName(name)
		
	def chooseRace(self):
		print("//----------// //----------// //----------// //----------//")
		print("Choose your race: ")
		print("Enter 1 for Dwarf")
		print("Enter 2 for Elf")
		race = input()
		print("//----------// //----------// //----------// //----------//")
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
