import random
import os
from art import logo
cards= [11,2,3,4,5,6,7,8,9,10,10,10,10]


def deal(hand):
    if hand:
        card = random.choice(cards)
        if card == 11 and 11 in hand:
            card = 1
        hand.append(card)
        return hand
    else:
        c1 = random.choice(cards)
        c2 = random.choice(cards)
        return [c1,c2]


def total(list):
    return sum(list)

def comparison(ptotal, dtotal):
    if dtotal == 21:
        return "Dealer Wins"
    elif ptotal > 21:
        return "Dealer Wins"
    elif dtotal > 21:
        return "Player Wins"
    elif dtotal == ptotal:
        return "Draw"
    elif ptotal > dtotal:
        return "Player Wins"
    else:
        return "Dealer Wins"


def play():
    os.system('cls')
    print(logo)
    phand = []
    dhand = []
    phand = deal(phand)
    dhand = deal(dhand)
    ptotal = total(phand)
    print(f"Your cards: {phand} {ptotal}")
    print(f"Dealer's first card: {dhand[0]}")
    if total(dhand) == 21 or ptotal == 21:
        reveal = True
    else:
        reveal = False
    while not reveal:
        if input("Type 'y' to get another card, type 'n' to pass: ") == "y":
            phand = deal(phand)
            ptotal = total(phand)
            print(f"Your hand: {phand} {ptotal}")
            if ptotal >= 21:
                reveal = True
        else:
            reveal = True

    while total(dhand) < 17 and total(dhand) < ptotal:
        dhand = deal(dhand)

    dtotal = total(dhand)

    print(f"Your final hand: {phand} {ptotal}")
    print(f"Dealer's final hand: {dhand} {dtotal}")
    print(comparison(ptotal, dtotal))

play_game = True
while play_game == True:
    play()
    if not input("Do you want to play again? Type 'y' or exit: ") == "y":
        play_game = False
        


