import ComplexUnit as cu
import ComplexValue as cv

a = cv.ComplexValue(20, cu.joule)
b = cv.ComplexValue(3, cu.second)
c = cv.divide(a, b)
cv.show(c)
