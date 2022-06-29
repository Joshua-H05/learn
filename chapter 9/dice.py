from random import randint


class Dice:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        value = randint(1, self.sides)
        print(f"The number you got is {value}!")


die_1 = Dice()
die_1.roll_die()
die_2 = Dice(10)
die_3 = Dice(20)
[die_2.roll_die() for value in range(10)]
[die_3.roll_die() for value in range(10)]
