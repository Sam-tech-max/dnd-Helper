import Spell

class SpellBook:
	def __init__(self, spellsKnown=0, spellSlot0=0, spellSlot1=1, spellSlot2=2,
	spellSlot3=3, spellSlot4=4, spellSlot5=5, spellSlot6=6, spellSlot7=7,
	spellSlot8=8, spellSlot9=9):
		list = []
		while(spellsKnown > 0):
			list.append(Spell.Spell())
			spellsKnown = spellsKnown - 1
		self.spells = list
		list = []
		list.append(spellSlot0)
		list.append(spellSlot1)
		list.append(spellSlot2)
		list.append(spellSlot3)
		list.append(spellSlot4)
		list.append(spellSlot5)
		list.append(spellSlot6)
		list.append(spellSlot7)
		list.append(spellSlot8)
		list.append(spellSlot9)
		self.spellSlot = list

	def printSpellBook(self):
		for spell in self.spells:
			spell.printSpell()
		index = 0
		for slot in self.spellSlot:
			print("Spell Slot " + str(index) + ": " + str(slot))
			index = index + 1
# //---------// //---------// //---------//
# get and set functions
# //---------// //---------// //---------//
