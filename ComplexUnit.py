# Author: Jonathan Zwiebel
# Version: 15 April 2017

class ComplexUnit(object):
	def __init__(self, unit_map):
		zeroes = []
		for unit in unit_map:
			if unit_map[unit] == 0:
				zeroes.append(unit)
		for unit in zeroes:
			del unit_map[unit]
		self.unit_map = unit_map

	def get_unit_map(self):
		return self.unit_map

	def to_string(self):
		if len(self.unit_map) == 0:
			return  ""
		out = ""
		for base_unit in self.unit_map:
			exponent = self.unit_map[base_unit]
			if exponent == 0:
				out += ""
			elif exponent == 1:
				out += base_unit + " "
			else:
				out += base_unit + "^" + str(exponent) + " "
		return out

def equals(cu1, cu2):
	print cu1.to_string()
	print cu2.to_string()
	for base_unit in cu1.get_unit_map():
		if base_unit not in cu2.get_unit_map():
			#print "First has " + base_unit + " which second doesn't have"
			return False
		if cu1.get_unit_map()[base_unit] != cu2.get_unit_map()[base_unit]:
			return False
	for base_unit in cu2.get_unit_map():
		if base_unit not in cu1.get_unit_map():
			#print "Second has " + base_unit + " which first doesn't have"
			return False
	return True