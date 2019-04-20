def function1():
    print("ahahhaha")
print("za funkcja")

function1()
function1()


def function2(x):
    return x ** 2

a = function2(3)

print(a)

def pow(x, y):
    return x ** y

print(pow(5,2))

def fun5(some_argument):
    print(some_argument)
    print("nieeeee")

fun5("fjkkjdsfnkjf")


#BMI calc

def bmi_calc(name, height, weight):
    bmi = weight / (height ** 2)
    print("bmi: ")
    print(bmi)
    if bmi < 25:
        return name + " brak nadwagi"
    else:
        return name + " ma nadwage"


print(bmi_calc("filip", 1.75, 73))