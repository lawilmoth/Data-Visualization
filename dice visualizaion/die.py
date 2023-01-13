from random import randint

class Die:
    #This class represents a single die
    #It should accept the number of sides on the dice
    #It should have a method called roll
    def __init__(self, num_sides=6) -> int:
        self.num_sides = num_sides

    def roll(self):
        return randint(1, self.num_sides)

        