import numpy as np
import collections
import cards as c
import deck as d
import gamemanager as g
import random
import os
import sys

def test():
    game = g.GameManager(d.Deck())
    for i in range(10000):
        game.deal()
        print(game.deck.length)
    assert(game.deck.length == (52 - 10000*4)%52)
    game.printHand(game.player_hand)
    for i in range(10000):
        game.deal()
        for j in range(5):
            game.hit(game.player_hand)
            game.printHand(game.player_hand)

test()
