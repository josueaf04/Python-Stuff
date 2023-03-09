#Clase del objeto deck 

import card
import random

# Constantes
suits = ('\u2764', '\u2666', '\u2660', '\u2618')
ranks = ('2', '3', '4', '5', '6', '7', '8', '9', 'J', 'Q', 'K', 'A')

class deck:

    def init(self): 
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
    
