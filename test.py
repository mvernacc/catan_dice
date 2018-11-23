from __future__ import division
import numpy as np
from dice import Dice_roller


def test_freq(dice_dict):
    dr = Dice_roller()
    results = np.zeros(13)
    n_rolls = 10000

    for i in range(n_rolls):
        x = dr.roll()
        results[x] += 1

    print 'Observed frequencies:'
    for x in range(13):
        of = results[x] / n_rolls
        f = dice_dict[x]
        print 'p({:d}) = {:.4f} (should be {:.4f})'.format(
            x, of, f)
        if abs(f - of) > 10 / n_rolls:
            print '^ WARNING INNACCURACY'


if __name__ == '__main__':
    dice_dict = # TODO
    test_freq(dice_dict)

