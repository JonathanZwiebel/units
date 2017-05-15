import ComplexUnit as cu
import ComplexValue as cv

momentum_system = {"kg":1, "m":1}
momentum = cu.ComplexUnit(momentum_system)
print momentum.to_string()

newton_system = {"m":1, "s": -2, "kg":1}
newton = cu.ComplexUnit(newton_system)
print newton.to_string()

x = cv.ComplexValue(5, newton)
y = cv.ComplexValue(7, newton)
a = cv.ComplexValue(12, momentum)
b = cv.ComplexValue(17, momentum)

print ("\n")

print cv.negate(x).to_string()
print cv.add(x, y).to_string()
print cv.add(x, a).to_string()
print cv.subtract(x, y).to_string()
print cv.subtract(y, x).to_string()
print cv.add(a, b).to_string()