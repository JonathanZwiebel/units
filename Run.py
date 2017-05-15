import ComplexUnit as cu
import ComplexValue as cv

t = cv.ComplexValue(6, cu.second)
v0 = cv.ComplexValue(20, cu.meterspersecond)
x0 = cv.ComplexValue(15, cu.meter)

g = cv.ComplexValue(-9.8, cu.meterspersecondsquared)
half = cv.ComplexValue(0.5, cu.unitless)

distance = cv.add(cv.multiply(t, t, g, half), cv.multiply(v0, t), x0)
cv.show(distance)