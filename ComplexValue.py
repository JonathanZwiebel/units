# Author: Jonathan Zwiebel
# Version: 15 April 2017

import ComplexUnit as cu

class ComplexValue(object):
	# A class for holding a complex value consisting of a single number and a combination of 
	# units with powers

	# value should be a number
	# unit should be a complex unit
	def __init__(self, value, unit):
		if unit == "invalid":
			self.valid = False
		else:
			self.value = value
			self.unit = unit
			self.valid = True

	def get_is_valid(self):
		return self.valid

	def get_value(self):
		return self.value

	def get_unit(self):
		return self.unit

	def set_value(self, value):
		self.value = value

	def set_unit(self, unit):
		self.unit = unit

	def to_string(self):
		if not self.valid:
			return "invalid"
		return str(self.value) + " " + self.unit.to_string()

si_library = {}
derived_library = {}

si_library["unitless"] = cu. unitless
si_library["kilogram"] = cu.kilogram
si_library["second"] = cu.second
si_library["ampere"] = cu.ampere
si_library["kelvin"] = cu.kelvin
si_library["candela"] = cu.candela
derived_library["hertz"] = cu. hertz
derived_library["meterspersecond"] = cu.meterspersecond
derived_library["meterspersecondsquared"] = cu.meterspersecondsquared
derived_library["kilogrammeter"] = cu.kilogrammeter
derived_library["kelvin"] = cu.kelvin
derived_library["meterssquared"] = cu.meterssquared
derived_library["meterscubed"] = cu. meterscubed
derived_library["newton"] = cu.newton
derived_library["joule"] = cu.joule
derived_library["watt"] = cu.watt
derived_library["pascal"] = cu.pascal
derived_library["coulomb"] = cu.coulomb
derived_library["volt"] = cu.volt
derived_library["farad"] = cu.farad
derived_library["ohm"] = cu. ohm
derived_library["siemen"] = cu.siemen
derived_library["weber"] = cu.weber
derived_library["tesla"] = cu.tesla
derived_library["henry"] = cu.henry

standard_library = si_library.copy()
standard_library.update(derived_library)

def unit_lookup(library, unit):
	for comparison_unit in library:
		if cu.equals(unit, library[comparison_unit]):
			return comparison_unit
	return unit.to_string()

def show(complex_value):
	if complex_value.get_is_valid():
		unitname = unit_lookup(standard_library, complex_value.get_unit())
		print str(complex_value.get_value()) + " " + unitname
	else:
		print "invalid"

# Negate a complex value
def negate(cv):
	return ComplexValue(-cv.get_value(), cv.get_unit())

# Add two ComplexValues
def add(*cvs):
	cv1 = cvs[0]
	value_sum = cv1.get_value()
	for i in range(1, len(cvs)):
		if not cu.equals(cv1.get_unit(), cvs[i].get_unit()):
			print "Unit mismatch: " + unit_lookup(standard_library, cv1.get_unit()) + " against " + unit_lookup(standard_library, cvs[i].get_unit())
			return ComplexValue(0, "invalid")
		value_sum += cvs[i].get_value()
	return ComplexValue(value_sum, cv1.get_unit())

# Subtract two ComplexValues
def subtract(cv1, cv2):
	return add(cv1, negate(cv2))

def multiply(*cvs):
	units = []
	new_value = 1
	for cv in cvs:
		units.append(cv.get_unit())
		new_value *= cv.get_value()
	return ComplexValue(new_value, cu.multiply(*tuple(units)))

def divide(cv1, cv2):
	return ComplexValue(cv1.get_value() / cv2.get_value(), cu.divide(cv1.get_unit(), cv2.get_unit()))