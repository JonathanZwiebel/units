import ComplexUnit as cu
import ComplexValue as cv

a = cv.ComplexValue(20.0, cu.watt)
b = cv.ComplexValue(14.0, cu.watt)
c = cv.ComplexValue(7.0, cu.watt)
d = cv.ComplexValue(-845, cu.watt)

f = cv.add(a, b, c, d)
cv.show(f)