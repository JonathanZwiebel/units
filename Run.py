import ComplexUnit as cu
import ComplexValue as cv

kilogram_system = {"kg":1, "m":0, "s":0}
kilogram = cu.ComplexUnit(kilogram_system)

meter_system = {"kg":0, "m":1, "s":0}
meter = cu.ComplexUnit(meter_system)

second_system = {"kg":0, "m":0, "s":1}
second = cu.ComplexUnit(second_system)

velocity_system = {"kg":0, "m":1, "s":-1}
velocity = cu.ComplexUnit(velocity_system)

acceleration_system = {"kg":0, "m":1, "s":-2}
acceleration = cu.ComplexUnit(acceleration_system)

momentum_system = {"kg":1, "m":1, "s":0}
momentum = cu.ComplexUnit(momentum_system)

newton_system = {"kg":1, "m":1, "s":-2}
newton = cu.ComplexUnit(newton_system)

x = cv.ComplexValue(5, kilogram)
y = cv.ComplexValue(7, acceleration)
xy = cv.multiply(x, y)

z = cv.ComplexValue(12, newton)
print cv.add(xy, z).to_string()