#Clase del objeto deck 

import os
import random

decks = 2
deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]*(int(decks)*4)

class deck: 
    def __init__(self): 
        self.deck = [] 
        for suit in suits: 
            for rank in ranks: 
                self.deck.append(card.card(suit, rank))

                
# Función que mezcla el deck

    def shuffle(self): 
        random.shuffle(self.deck)


# Función que reparte las cartas 

    def deal(self): 
        onecard = self.deck.pop()
        return onecard                    
    
    
