import numpy as np
import collections
import cards as c
import deck as d
import random
import os
import sys

name = "Blackjack"
gameDeck = d.Deck()
player_score = 0

def main():
    gameDeck.shuffle()
    os.system('clear')
    print("Welcome to {}!".format(name))
    print('\n\n\n\n\n')
    input("Press Enter to Play")
    game(gameDeck)


def game(gameDeck):
    os.system('clear')
    dealer_hand = gameDeck.deal()
    player_hand = gameDeck.deal()
    choice = 0
    while choice != "q":
        print("Place your bet!")
        print("Dealer's Hand: " + handToString(dealer_hand[:1], True))
        print("Your Hand: " + handToString(player_hand) + "Your Hand's Value: " + str(handValue(player_hand)))
        blackjack(dealer_hand, player_hand)
        choice = input("Do you want to [H]it, [S]tand, [P]oints, or [Q]uit: ").lower()
        os.system('clear')
        if choice == "h":
            gameDeck.hit(player_hand)
            checkBust(dealer_hand, player_hand)
            print(gameDeck.length)
        elif choice == "s":
            while handValue(dealer_hand) < 17:
                gameDeck.hit(dealer_hand)
            checkBust(dealer_hand, player_hand)
            score(dealer_hand, player_hand)
            play_again()
        elif choice == "p":
            print("You have " + str(player_score) + " points")
        elif choice == "q":
            print("Bye!")
            sys.exit()

def updatePoints(win, blackjack = False):
    global player_score
    if blackjack:
        player_score += 2
    else:
        player_score += 1
    return player_score

def score(dealer_hand, player_hand):
    player_value, dealer_value = handValue(player_hand), handValue(dealer_hand)
    if dealer_value > player_value:
        print_results(dealer_hand, player_hand)
        print("The dealer has a better hand than you... You lose!")
    elif player_value > dealer_value:
        print_results(dealer_hand, player_hand)
        updatePoints()
        print("You have a better hand than the dealer! You win!")

def checkBust(dealer_hand, player_hand):
    player_value, dealer_value = handValue(player_hand), handValue(dealer_hand)
    if (dealer_value > 21):
        print_results(dealer_hand, player_hand)
        print("Dealer busted! You win!")
        play_again()
    elif (player_value > 21):
        print_results(dealer_hand, player_hand)
        print("Sorry you bust.")
        play_again()


def play_again():
    again = input("Do you want to play again? (Y/N) : ").lower()
    if again == "y":
	    dealer_hand = []
	    player_hand = []
	    deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]*4
	    game(gameDeck)
    elif again == "n":
	    print("Bye!")
	    sys.exit()
    else:
        print("That's not a valid input!")
        play_again()

def print_results(dealer_hand, player_hand):
    os.system('clear')
    print("The dealer has a " + handToString(dealer_hand) + " for a total of " + str(handValue(dealer_hand)))
    print("You have a " + handToString(player_hand) + " for a total of " + str(handValue(player_hand)))

def blackjack(dealer_hand, player_hand):
    if handValue(player_hand) == 21:
        print_results(dealer_hand, player_hand)
        print("Congratulations! You got a Blackjack! Double Points!\n")
        updatePoints(True)
        play_again()
    elif handValue(dealer_hand) == 21:
        print_results(dealer_hand, player_hand)
        print("Sorry, you lose. The dealer got a blackjack.\n")
        play_again()

def handValue(hand):
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

def join_lines(strings):
    string_lines = [string.splitlines() for string in strings]
    return '\n'.join(''.join(out_line) for out_line in zip(*string_lines))

def printHand(hand):
    guis = [card.gui for card in hand]
    print(join_lines(guis))

def handToString(hand, d = False):
    guis = [card.gui for card in hand]
    if d == True:
        guis = [c.Card.blank] + guis
    return "\n" + join_lines(guis) + "\n"


main()
