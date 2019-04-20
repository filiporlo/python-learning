class Robot:
    def __init__(self, name, color, weight):
        self.name = name
        self.color = color
        self.weight = weight
    def introduce_self(self):
        print("My name is " + self.name)

r1 = Robot("tom", "red",80 )
r2 = Robot("anna", "green", 50)

r1.introduce_self()
r2.introduce_self()


class Person:
    def __init__(self, name, personality, issitting, robot):
        self.name = name
        self.personality = personality
        self.issitting = issitting
        self.robot = robot

    def sit_down(self):
        self.issitting = True

    def stand_up(self):
        self.issitting = False


p1 = Person("Alice", "female", False, r2)
p2 = Person("Maciek", "male", True, r1)

p1.robot.introduce_self()
p2.robot.introduce_self()

p1.robot = r1
p2.robot = r2

p1.robot.introduce_self()
p2.robot.introduce_self()
