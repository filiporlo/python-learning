import numpy as np
import scipy as sp

a = np.arange(9)

b = np.median(a)

d = np.reshape(a,(3,3))
w = np.random.rand(3,3)

x = np.random.rand(3,3)

y = np.dot(w,x)

print(y)

print(b)
print(w)
print(d)