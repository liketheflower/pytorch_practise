# this code is used to buid a graph based on the numpy
# jimmy shen
# April 1, 2018


import numpy as np
np.random.seed(0)

N, D =3, 4

x = np.random.randn(N, D)
y = np.random.randn(N, D)
z = np.random.randn(N, D)

a = x*y
b = a+z
c = np.sum(b)
print("x", x)
print('y',y)
print('z',z)
print('a',a)
print('b',b)
print('c',c)