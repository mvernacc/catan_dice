from __future__ import division


def get_dice_dict_2_6():
    """Make a probability dictionary for the sum of
    two 6-sided dice."""
    dice_dict = dict()
    for x in range(2, 13)
        dice_dict[x] = (6 - abs(x - 7)) / 36.
