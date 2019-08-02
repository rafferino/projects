import numpy as np
import collections
import cards as c
import deck as d
import random
import os

class Hand:

    def __init__(self, cards, value):
        self.cards = cards
        self.value = sum([card.number for card in cards])

    def handValue(self, hand):
        return sum([card.number for card in hand])

    def updateHandValue(self, card):
        val = card.value
        

    def join_lines(strings):
        string_lines = [string.splitlines() for string in strings]
        return '\n'.join(''.join(out_line) for out_line in zip(*string_lines))

    def __str__(hand):
        guis = [card.gui for card in hand]
        return join_lines(guis)

    def handToString(hand):
        guis = [card.gui for card in hand]
        return "\n" + join_lines(guis) + "\n"
