from __future__ import division


def get_dice_dict_2_6():
    """Make a probability dictionary for the sum of
    two 6-sided dice."""
    dice_dict = dict()
    for x in range(2, 13):
        dice_dict[x] = (6 - abs(x - 7)) / 36.
    return dice_dict


def get_dice_dict_1_6():
    """Make a probability dictionary for one 6-sided die."""
    dice_dict = dict()
    for x in range(1, 7):
        dice_dict[x] = 1 / 6.
    return dice_dict
