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
			
	def chooseDwarf(self):
		print("You Choose Dwarf")
		player = self.getPlayer()
		player.setRace("Dwarf")
		constitution = player.getStats().getStat("constitution")
		constitution.setScore(constitution.getScore() + 2)
		self.chooseAge("What is the age of your Dwarf? Dwarves mature at the same rate as humans, but they're considered young until they reach the age of 50. On average, they live about 350 years.")
		self.chooseAlignment("Most dwarves are lawful, believing firmly in the benefits of a well-ordered society. They tend toward good as well, with a strong sense of fair play and a belief that everyone deserves to share in the benefits of a just order.")
		player.setSpeed(25)

	def choosePlayerName(self):
		name = input("Please enter your name: ")
		self.getPlayer().setPlayerName(name)
		
	def chooseRace(self):
		print("Choose your race: ")
		print("Enter 1: Dwarf")
		race = input()
		if(race == "1"):
			print("Race = Dwarf")
			self.chooseDwarf()
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
