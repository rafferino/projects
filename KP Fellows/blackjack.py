import numpy as np
import collections
import cards as c
import deck as d
import gamemanager as g
import random
import os
import sys

name = "Blackjack"
game = g.GameManager(d.Deck())
print(game.deck)

def bankrupt():
    if game.bankrupt():
        if input("Do you want to start a new game? (Y/N)").lower() == 'y':
            game.chips = 100
            main()
        else:
            sys.exit()

def play_again():
    bankrupt()
    again = input("Do you want to play again? (Y/N) : ").lower()
    if again == "y":
        play()

    elif again == "n":
        print("Bye!")
        sys.exit()
    else:
        print("That's not a valid input!")
        play_again()

def main():
    game.deck.shuffle()
    os.system('clear')
    print("Welcome to {}!".format(name))
    print('\n\n\n\n\n')
    input("Press Enter to Play\n")
    play()


def play():
    bankrupt()
    os.system('clear')
    check = game.place_bet()
    if not check:
        play_again()
    game.deal()
    choice = 0
    round = 0
    while choice != "q":
        game.show()
        if round == 0:
            b = game.blackjack()
            if b:
                play_again()
        choice = input("Do you want to [H]it, [S]tand, check [C]hips, or [Q]uit: ").lower()
        os.system('clear')
        if choice == "h":
            game.hit(game.player_hand)
            if game.checkBust():
                play_again()
        elif choice == "s":
            game.stay()
            b = game.checkBust()
            if b:
                play_again()
            game.score()
            play_again()
        elif choice == "c":
            game.check()
        elif choice == "q":
            print("Bye!")
            sys.exit()
        round += 1

main()
