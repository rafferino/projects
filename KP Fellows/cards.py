import numpy as np
import collections

class Card:
    values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

    suits = ['Spades', 'Diamonds','Hearts','Clubs']

    name_to_symbol = {
        'Spades':   '♠',
        'Diamonds': '♦',
        'Hearts':   '♥',
        'Clubs':    '♣',
    }

    blank = (
        '┌─────────┐\n'
        '│░░░░░░░░░│\n'
        '│░░░░░░░░░│\n'
        '│░░░░░░░░░│\n'
        '│░░░░░░░░░│\n'
        '│░░░░░░░░░│\n'
        '│░░░░░░░░░│\n'
        '│░░░░░░░░░│\n'
        '└─────────┘'
    )

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
        try:
            self.number = int(self.value)
        except:
            if self.value == 'A':
                self.number = 11
            else:
                self.number = 10
        self.symbol = Card.name_to_symbol[suit]
        self.gui = (
            '┌─────────┐\n'
            '│{}       │\n'
            '│         │\n'
            '│         │\n'
            '│    {}   │\n'
            '│         │\n'
            '│         │\n'
            '│       {}│\n'
            '└─────────┘'
        ).format(
            format(self.value, ' <2'),
            format(self.symbol, ' <2'),
            format(self.value, ' >2')
        )

    def __str__(self):
        return self.gui
