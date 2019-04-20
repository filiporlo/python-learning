total = 0


for i in range(1,5):
    total += i

print(total)


total1 = 0
j=1
while j < 5:
    total1 += j
    j += 1
print(total1)


given_list = [5,4,4,2,1,-5]

total3 = 0

i = 0
while i < len(given_list) and given_list[i] > 0:
    total3 += given_list[i]
    i += 1

print(total3)


given_list2 = [5,4,4,3,1,-2,-2,-3,-5]

total4 = 0

for e in given_list2:
    if e <= 0:
        break
    total4 += e

print(total4)


total4 = 0
i = 0
while True:
    total4 += given_list2[i]
    i += 1
    if given_list2[i] <= 0:
        break

print(total4)



given_list3 = [5,4,3,-2,-3,-7]
total5 = 0
for e in given_list3:
    if e <= 0:
        total5 += e

print(total5)


