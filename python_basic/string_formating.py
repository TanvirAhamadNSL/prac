
import numpy as np
from numpy import pi
import cmath

a = np.ones(3, dtype=np.int32)
b = np.linspace(0, pi, 3)
c = a+b
d = np.exp(c * 1j)
#a = np.ones((2, 3), dtype=int)
#b = rg.random((2, 3))
print(d)


# rg = np.random.default_rng(12)
# a = np.ones((2, 3), dtype=int)
# b = rg.random((2, 3))
# print(b)
