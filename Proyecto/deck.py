#Clase del objeto deck 

import os
import random

decks = 2
deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]*(int(decks)*4)

import main
class deck:
    def play_again():
        again = input("Quieres seguir jugando? (Y/N) : ").lower()
        if again == "y":
            dealer_hand = []
            player_hand = []
            deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]*4
            main.Game()
        else:
            print("ADIOS!")
            exit()

    def shuffle(self): 
        random.shuffle(self.deck)
# Función que reparte las cartas 

    def deal(self): 
        onecard = self.deck.pop()
        return onecard                    
    
    
