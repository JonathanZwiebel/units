import ComplexUnit as cu
import ComplexValue as cv

unitless = cu.ComplexUnit({})
kilogram = cu.ComplexUnit({"kg":1})
meter = cu.ComplexUnit({"m":1})
second = cu.ComplexUnit({"s":1})
ampere = cu.ComplexUnit({"A":1})
kelvin = cu.ComplexUnit({"K":1})
candela = cu.ComplexUnit({"cd":1})
si_library = [unitless, kilogra, meter, second, ampere, kelvin, candela]

hertz = cu.reciprocal(second)
meterpersecond = cu.divide(meter, second)
meterpersecondsquared = cu.divide(meterpersecond, second)
kilogrammeter = cu.multiply(meter, kilogram)
metersquared = cu.multiply(meter, meter)
metercubed = cu.multiply(metersquared, meter)
newton = cu.multiply(meterpersecondsquared, kilogram)
joule = cu.multiply(newton, meter)
watt = cu.divide(joule, second)
pascal = cu.divide(newton, metersquared)
coulomb = cu.multiply(second, ampere)
volt = cu.divide(watt, ampere)
farad = cu.divide(coulomb, volt)
ohm = cu.divide(volt, ampere)
siemen = cu.reciprocal(ohm)
weber = cu.divide(joule, ampere)
tesla = cu.divide(weber, metersquared)
henry = cu.divide(weber, ampere)
derived_library = [hertz, meterpersecond, meterpersecondsquared, kilogrammeter, metersquared, metercubed, newton, joule, watt, pascal, coulomb, volt, farad, ohm, siemen, weber, tesla, henry]

standard_library = si_library + derived_library

