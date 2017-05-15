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

# Negate a complex value
def negate(cv):
	return ComplexValue(-cv.get_value(), cv.get_unit())

# Add two ComplexValues
def add(cv1, cv2):
	if not cu.equals(cv1.get_unit(), cv2.get_unit()):
		print "Unit mismatch: " + cv1.get_unit().to_string() + "against " + cv2.get_unit().to_string()
		return ComplexValue(0, "invalid")
	return ComplexValue(cv1.get_value() + cv2.get_value(), cv1.get_unit())

# Subtract two ComplexValues
def subtract(cv1, cv2):
	return add(cv1, negate(cv2))

def multiply(cv1, cv2):
	return ComplexValue(cv1.get_value() * cv2.get_value(), cu.multiply(cv1.get_unit(), cv2.get_unit()))

def divide(cv1, cv2):
	return ComplexValue(cv1.get_value() / cv2.get_value(), cu.divide(cv1.get_unit(), cv2.get_unit()))