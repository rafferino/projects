import numpy as np
import collections
import random
import cards as c

class Deck:
    def __init__(self):
        self.deck = [c.Card(suit, value) for value in c.Card.values for suit in c.Card.suits]
        self.length = len(self.deck)

    def splitDeck(self):
        return self.deck[:self.length//2], self.deck[self.length//2:]

    def shuffle(self):
        random.shuffle(self.deck)

    def reshuffle(self):
        self.deck = [c.Card(suit, value) for value in c.Card.values for suit in c.Card.suits]
        self.shuffle()
        self.length = len(self.deck)

    def deal(self):
        newHand = []
        for i in range(2):
            self.checkDeck()
            self.length -= 1
            newHand.append(self.deck.pop())
        return newHand

    def hit(self, hand):
        self.checkDeck()
        self.length -= 1
        return hand.append(self.deck.pop())

    def checkDeck(self):
        if self.length <= 0:
            self.reshuffle()

    def __str__(self):
        # deckString = [str(card.value) + ", " + str(card.suit) + ", " + str(card.symbol) for card in self.deck]

        deckString = [card.gui for card in self.deck]

        return "\n".join(deckString)
