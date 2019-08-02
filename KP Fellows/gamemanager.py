import numpy as np
import collections
import cards as c
import deck as d
import random
import os
import sys


class GameManager:

    def __init__(self, deck):
        self.chips = 100
        self.deck = deck
        self.bet = 0
        self.dealer_hand = None
        self.player_hand = None

    def place_bet(self):
        print("You have {} chips!".format(self.chips))
        temp = input("Place your bets!\n")
        try:
            temp = int(temp)
        except:
            if temp == 'q':
                print('Bye!')
                sys.exit()
            print("That is not a valid bet!")
            return False
        if temp <= self.chips and temp > 0:
            self.bet = temp
        else:
            print("That is not a valid bet!")
            return False
        return True

    def deal(self):
        self.dealer_hand = self.deck.deal()
        self.player_hand = self.deck.deal()

    def hit(self, hand):
        self.deck.hit(hand)

    def show(self):
        print("Dealer's Hand: " + self.handToString(self.dealer_hand[:1], True))
        print("Your Hand: " + self.handToString(self.player_hand) + "Your Hand's Value: " + str(self.handValue(self.player_hand)))

    def handValue(self, hand):
        total = 0
        for card in hand:
            val = card.value
            if val == "J" or card == "Q" or card == "K":
                total+= 10
            elif val == "A":
                if total >= 11: total+= 1
                else: total+= 11
            else:
                total += card.number
        return total

    def join_lines(self, strings):
        string_lines = [string.splitlines() for string in strings]
        return '\n'.join(''.join(out_line) for out_line in zip(*string_lines))

    def printHand(self, hand):
        guis = [card.gui for card in hand]
        print("\n" + self.join_lines(guis) + "\n")

    def handToString(self, hand, d = False):
        guis = [card.gui for card in hand]
        if d == True:
            guis = [c.Card.blank] + guis
        return "\n" + self.join_lines(guis) + "\n"

    def print_results(self):
        os.system('clear')
        print("The dealer has a " + self.handToString(self.dealer_hand) + "for a total of " + str(self.handValue(self.dealer_hand)))
        print("You have a " + self.handToString(self.player_hand) + "for a total of " + str(self.handValue(self.player_hand)))

    def blackjack(self):
        if self.handValue(self.player_hand) == 21:
            self.print_results()
            print("Congratulations! You got a Blackjack! Double Points!\n")
            self.chips += self.bet*2
            print("You won {0} chips for a running total of {1}".format(self.bet*2, self.chips))
            return True
        elif self.handValue(self.dealer_hand) == 21:
            self.print_results()
            print("Sorry, you lose. The dealer got a blackjack.\n")
            self.chips -= self.bet
            print("You lost {0} chips for a running total of {1}".format(self.bet, self.chips))
            return True
        return False

    def checkBust(self):
        player_value, dealer_value = self.handValue(self.player_hand), self.handValue(self.dealer_hand)
        if (dealer_value > 21):
            self.print_results()
            print("Dealer busted! You win!")
            self.chips += self.bet
            return True
        elif (player_value > 21):
            self.print_results()
            print("Sorry you bust.")
            self.chips -= self.bet
            return True
        return False

    def stay(self):
        while self.handValue(self.dealer_hand) < 17:
            self.hit(self.dealer_hand)

    def score(self):
        player_value, dealer_value = self.handValue(self.player_hand), self.handValue(self.dealer_hand)
        if dealer_value > player_value:
            self.print_results()
            print("The dealer has a better hand than you... You lose!")
            self.chips -= self.bet
            print("You lost {0} chips for a running total of {1}".format(self.bet, self.chips))
        elif player_value > dealer_value:
            self.print_results()
            self.chips += self.bet
            print("You have a better hand than the dealer! You win!")
            print("You won {0} chips for a running total of {1}".format(self.bet, self.chips))
        elif dealer_value == player_value:
            self.print_results()
            print("You and the dealer tied!")

    def check(self):
        print("You have " + str(self.chips) + " chips!")

    def bankrupt(self):
        if self.chips <= 0:
            print("You've gone bankrupt! Try again some other time!")
            return True
        return False
