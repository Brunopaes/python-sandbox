# -*- coding: utf-8 -*-
import random


def furigoma(bo, iterator_):
    """Simple function used in shogi to decide which player will begin the
    match.

    Parameters
    ----------
    bo : int
        Best Of (Number of Decider "matches").

    iterator_ : iterator
        list or tuple with player names.

    Returns
    -------

    """
    for i in range(bo):
        print(random.choice(iterator_))


if __name__ == '__main__':
    furigoma(5, ('bruno', 'caio'))
