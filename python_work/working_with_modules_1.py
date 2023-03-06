from random import randint

x = randint(1,6)

class Die():
    """Working with the properties of a dice"""
    def __init__(self,sides):
        self.sides = sides

    def roll_die(self):
        if self.sides == 10:
            x = randint(1,10)
        elif self.sides == 20:
            x = randint(1,20)
        elif self.sides == 6:
             x = randint(1,6)
        print('The number obtained from rolling the dice ' + str(x))

six_sided_dice = Die(6)
six_sided_dice.roll_die()
six_sided_dice.roll_die()
six_sided_dice.roll_die()
six_sided_dice.roll_die()
six_sided_dice.roll_die()

print("\nThese trials are for the 10-faced die: ")
ten_sided_dice = Die(10)
ten_sided_dice.roll_die()
ten_sided_dice.roll_die()
ten_sided_dice.roll_die()
ten_sided_dice.roll_die()
ten_sided_dice.roll_die()
ten_sided_dice.roll_die()
ten_sided_dice.roll_die()

print("\nThese trials are for the 20-faced die: ")
twenty_sided_dice = Die(20)
twenty_sided_dice.roll_die()
twenty_sided_dice.roll_die()
twenty_sided_dice.roll_die()
twenty_sided_dice.roll_die()
twenty_sided_dice.roll_die()