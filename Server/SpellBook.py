from typing import List
import Spell
Vector = List[Spell.Spell]


class SpellBook:
	def __init__(self, spellsKnown: int=0, spellSlot0: int=0,
			  spellSlot1: int=1, spellSlot2: int=2,
			  spellSlot3: int=3, spellSlot4: int=4,
			  spellSlot5: int=5, spellSlot6: int=6,
			  spellSlot7: int=7, spellSlot8: int=8,
			  spellSlot9: int=9, spellList: Vector=[Spell.Spell()]):
		
		initSpells = len(spellList)
		while(spellsKnown > initSpells):
			spellList.append(Spell.Spell())
			spellsKnown = spellsKnown - 1
		self.spells = spellList
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
	def getSpellByName(self, name: str) -> Spell.Spell:
		s = "empty"
		for spell in self.getSpells():
			if(spell.getName() == name):
				return spell

	def addSpell(self, spell: Spell.Spell):
		self.getSpells().append(spell)

	def getSpells(self) -> Vector:
		return self.spells

	def setSpellSlot(self, spellSlot:int, spellSlotsAvailable: int):
		if(spellSlotsAvailable >= 0):
			if(spellSlot >= 0 and spellSlot <= 9):
				self.spellSlot[spellSlot] = spellSlotsAvailable
			else:
				print("spell slot needs to be between 0 and 9.")
		else:
			print("spell slots availabe needs to be greater than or equal to 0.")


# //---------// //---------// //---------//
# main functions
# //---------// //---------// //---------//