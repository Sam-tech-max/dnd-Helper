import Player

def checkIfInt(value):
	if('int' in str(type(value))):
		return True
	else:
		print("Error :: incorrect type value :: need int")
		return False

def checkIfStr(value):
	if('str' in str(type(value))):
		return True
	else:
		print("Error :: incorrect type value :: need str")
		
def makePlayer():
	#inspiration=0, age=20
	print("Welcome to Character Maker")
	name = input("Please Enter Your Character's Name: ")
	classRole = input("Please Enter Your Character's Class: ")
	level = input("Please Enter Your Character's Level: ")
	background = input("Please Enter Your Character's Background: ")
	playerName = input("Please Enter Your Name: ")
	race = input("Please Enter Your Character's Race: ")
	alignment = input("Please Enter Your Character's Alignment: ")
	inspiration = input("Please Enter Your Character's Inspiration: ")
	age = input ("Please Enter Your Character's Age: ")
	player = Player.Player(name, classRole, level, background, playerName, race, alignment, inspiration, age)
	player.printPlayer()
	return player


class GameMaker:
	

	def __init__(self, playerCount=1):
		# Checks to see if player count is an integer
		if(checkIfInt(playerCount)):
			self.playerCount = playerCount
		else:
			print("Only one player in the game.")
			self.playerCount = 1
		count = playerCount
		self.players = list()
		while(count > 0):
			self.players.append(makePlayer())
			count -= 1

	def printPlayers(self):
		for player in self.players:
			player.printPlayer()
		
game = GameMaker()
#game.printPlayers()
