a = ["filip", "maciek", "karolina"]

for element in a:
    print(element)


b = [20,10,5]
total = 0
for e in b:
    print(e)
    total += e


print(total)

c = list(range(1,101))

print(c)

for i in range(1,5):
    print(i)


list(range(1,8))

total1 = 0

for i in range(1,8):
    if (i % 3) == 0:
        total1 += i

print(total1)

total2 = 0
for i in range(1,100):
    if not i%3 and not i%5:
        total2 += i

print(total2)
