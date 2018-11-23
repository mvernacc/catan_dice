from __future__ import division
from dice import Dice_roller
from dice_dict import get_dice_dict_2_6


def test_freq(dice_dict):
    dr = Dice_roller()
    results = dict()
    for x in dice_dict:
        results[x] = 0
    n_rolls = 10000

    for i in range(n_rolls):
        x = dr.roll()
        results[x] += 1

    print 'Observed frequencies:'
    for x in dice_dict:
        of = results[x] / n_rolls
        f = dice_dict[x]
        print 'p({:d}) = {:.4f} (should be {:.4f})'.format(
            x, of, f)
        if abs(f - of) > 10 / n_rolls:
            print '^ WARNING INNACCURACY'


if __name__ == '__main__':
    dice_dict = get_dice_dict_2_6()
    test_freq(dice_dict)

