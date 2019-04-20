import numpy as np 

a = np.zeros((5,2))

print(a)

print("Ala ma kota")

c = np.arange(9).reshape(3,3)
d = np.arange(9).reshape(3,3)

z = np.dot(c,d)

print(c)
print(d)

x = np.median(c)

print(x)

print(z)