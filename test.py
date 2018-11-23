from __future__ import division
from dice import Dice_roller
from dice_dict import get_dice_dict_2_6


def test_freq(dice_dict):
    dr = Dice_roller(dice_dict, 10)
    results = dict()
    for x in dice_dict:
        results[x] = 0
    n_rolls = 10000

    for i in range(n_rolls):
        x = dr.query()
        # x = dr.roll()
        results[x] += 1

    print 'Observed frequencies:'
    for x in dice_dict:
        of = results[x] / n_rolls    # observed frequency
        f = dice_dict[x]    # ideal frequency
        # Std. dev. on observed frequency
        sd = (f * (1 - f) / n_rolls)**0.5

        print 'p({:d}) = {:.4f} (should be {:.4f} +/- {:.4f})'.format(
            x, of, f, 3 * sd)

        if abs(f - of) > 3 * sd:
            print '^ WARNING INNACCURACY'


if __name__ == '__main__':
    dice_dict = get_dice_dict_2_6()
    test_freq(dice_dict)

