# -*- coding: utf-8 -*-
import random


def best_of(bo, iterator_):
    """Function used for deciding something in Best of Something matches.

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


def furigoma():
    """Shogi starting player method.

    Parameters
    ----------

    Returns
    -------

    """
    pawn_state = ('normal', 'promoted')

    player_1 = []
    player_2 = []
    for pawn in range(5):
        player_1.append(random.choice(pawn_state))
        player_2.append(random.choice(pawn_state))

    return player_1.count(pawn_state[-1]), player_2.count(pawn_state[-1])


if __name__ == '__main__':
    list_ = []
    for i in range(10):
        list_.clear()
        for j in range(100000):
            play = furigoma()
            list_.append(play.index(max(play)) + 1)

        print('player 1: {}\nplayer 2: {}\n-------------'.format(
            list_.count(1), list_.count(2)
        ))
