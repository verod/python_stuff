#!/bin/python

class PartyAnymal:
	x = 0
	name = ""
	
	def __init__(self,nam):
		self.name = nam
		print self.name, "-> constructed"

	def party(self):
		self.x = self.x + 1
		print self.name, " party count ", self.x
	
	def __del__(self):
		print "I am dead", self.x

an = PartyAnymal("Ana")
bn = PartyAnymal("Bobo")

an.party()
bn.party()

an.party()
bn.party()

