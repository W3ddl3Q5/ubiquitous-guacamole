import random

class Dice:
    def roll(self):
        firstval = random.randint(0,6)
        secondval = random.randint(0,6)
        output = (firstval, secondval)
        return output
    
dice = Dice()
print(dice.roll())