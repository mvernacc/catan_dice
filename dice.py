from numpy.random import choice
import collections

class Dice_roller:

    def __init__(self, dice_dict, window_size):
        self.dice_dict = dice_dict
        self.keys = dice_dict.keys()
        self.window_size = window_size
        self.prev_rolls = collections.deque()
        for i in range(self.window_size):
            self.prev_rolls.append(None)
        self.thresholds = self.get_thresholds()
        self.counts = {}
        for key in self.keys:
            self.counts[key] = 0

    def query(self):
        p = [self.dice_dict[key] for key in self.keys]
        return choice(self.keys, 1, p=p)[0]

    def get_thresholds(self):
        thresholds = {}
        for key in self.keys:
            p = self.dice_dict[key]
            n = float(self.window_size)
            thresholds[key] = n*p + 2*((n*p*(1.0-p))**(0.5))
        return thresholds

    def roll(self):
        #pops old value
        old_value = self.prev_rolls.popleft()
        if old_value is not None:
            self.counts[old_value] -= 1

        found = False
        new_value = None
        while not found:
            new_value = self.query()
            found = self.counts[new_value] < (self.thresholds[new_value] - 1)
        self.counts[new_value] += 1        
        self.prev_rolls.append(new_value)
        return new_value

my_dice = {}
p = 0.5
my_dice[0] = p
my_dice[1] = 1-p
my_roller = Dice_roller(my_dice, 10)
print my_roller.prev_rolls
print my_roller.counts
for i in range(12):
    my_roller.roll()
    print my_roller.prev_rolls
    print my_roller.counts


        


        
