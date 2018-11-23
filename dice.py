from numpy.random import choice

class Dice_roller:

    def __init__(self, dice_dict, window_size):
        self.dice_dict = dice_dict
        self.keys = dice_dict.keys()
        self.window_size = window_size
        self.prev_rolls = [None for i in range(window_size)]

    def query(self):
        p = [self.dice_dict[key] for key in self.keys]
        print p
        return choice(self.keys, 1, p=p)[0]



        


        
