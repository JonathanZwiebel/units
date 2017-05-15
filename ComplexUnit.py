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

# Multiplies two units together by taking all of thier exponents and adding them together
def multiply(cu1, cu2):
	new_map = {}
	for base_unit in cu1.get_unit_map():
		if base_unit in cu2.get_unit_map():
			new_map[base_unit] = cu1.get_unit_map()[base_unit] + cu2.get_unit_map()[base_unit]
		else:
			new_map[base_unit] = cu1.get_unit_map()[base_unit]
	for base_unit in cu2.get_unit_map():
		if not base_unit in new_map:
			new_map[base_unit] = cu2.get_unit_map()[base_unit]
	return ComplexUnit(new_map)

# Returns a new ComplexUnit that is the reciprocal of this unit 
def reciprocal(cu):
	new_map = {}
	for base_unit in cu.get_unit_map():
		new_map[base_unit] = -cu.get_unit_map()[base_unit]
	return ComplexUnit(new_map)

def divide(cu1, cu2):
	return multiply(cu1, reciprocal(cu2))

unitless = ComplexUnit({})
kilogram = ComplexUnit({"kg":1})
meter = ComplexUnit({"m":1})
second = ComplexUnit({"s":1})
ampere = ComplexUnit({"A":1})
kelvin = ComplexUnit({"K":1})
candela = ComplexUnit({"cd":1})
hertz = reciprocal(second)
meterpersecond = divide(meter, second)
meterpersecondsquared = divide(meterpersecond, second)
kilogrammeter = multiply(meter, kilogram)
metersquared = multiply(meter, meter)
metercubed = multiply(metersquared, meter)
newton = multiply(meterpersecondsquared, kilogram)
joule = multiply(newton, meter)
watt = divide(joule, second)
pascal = divide(newton, metersquared)
coulomb = multiply(second, ampere)
volt = divide(watt, ampere)
farad = divide(coulomb, volt)
ohm = divide(volt, ampere)
siemen = reciprocal(ohm)
weber = divide(joule, ampere)
tesla = divide(weber, metersquared)
henry = divide(weber, ampere)