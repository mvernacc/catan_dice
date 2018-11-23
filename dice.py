from numpy.random import choice

class Dice_roller:

    def __init__(self, dice_dict, window_size):
        self.dice_dict = dice_dict
        self.keys = dice_dict.keys()
        self.window_size = window_size
        self.prev_rolls = [None for i in range(window_size)]

    def construct_thresholds(self):
        


    def query(self):
        p = [self.dice_dict[key] for key in self.keys]
        print p
        return choice(self.keys, 100, p=p)

my_dice = {}
p = 0.6
my_dice[0] = 1-p
my_dice[1] = p

my_roller = Dice_roller(my_dice, 10)
bob =  my_roller.query()
print len(bob)
print sum(bob)

        


        
