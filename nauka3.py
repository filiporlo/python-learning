print("hello 1")
print("hello 2")

a = 1
b = 3

if a < b:
    print("a mniejsze niz b")
    print("bbbbb")
print("nie wiadomo")

c = 3
d = 4
if c < d:
    print("c mniejsze niz d")
else:
    print("c nie jest mniejsze niz d")
print("za blokiem")

e = 8
f = 7

if e < f:
    print("e jest mniejsze niz f")
elif e == f:
    print("e jest rowne f")
else:
    print("e jest wieksze niz f")


name = "Filip"
height_m = 1.76
weight_kg = 90

bmi = weight_kg / (height_m ** 2)

print("bmi: ")
print(bmi)

if bmi<25:
    print(name)
    print("nie ma nadwagi")
else:
    print(name)
    print("jest nadwaga")