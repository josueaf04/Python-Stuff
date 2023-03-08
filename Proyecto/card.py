# Clase del objeto carta

import os
import random


class card:
    

    def deal(deck):
        hand = []
        for i in range(2):
            random.shuffle(deck)
            card = deck.pop()
            if card == 11:card = "J"
            if card == 12:card = "Q"
            if card == 13:card = "K"
            if card == 14:card = "A"
            hand.append(card)
        return hand

    def total(hand):
        total = 0
        for card in hand:
            if card == "J" or card == "Q" or card == "K":
                total+= 10
            elif card == "A":
                if total >= 11: total+= 1
                else: total+= 11
            else: total += card
        return total
    
   
    
    def clear():
        if os.name == 'nt':
            os.system('CLS')
        if os.name == 'posix':
            os.system('clear')