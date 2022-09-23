import cmath

number = complex(input())
print(abs(complex(number.real, number.imag)))
print(cmath.phase(complex(number.real, number.imag)))