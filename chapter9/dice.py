from random import choice
class Dice:
    def __init__(self, sides=6):
        self.sides=sides
    def roll_die(self):
        l=[]
        for i in range(self.sides):
            l.append(i)
        a=choice(l)
        print(f"this dice has {self.sides} sides and the chosen number is {a}")
p=Dice(6)
for i in range(10):
    p.roll_die()
a=Dice(10)
for i in range(10):
    a.roll_die()