# Main page

import deck
import hand
import utils

# values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
            #  'J': 10, 'Q': 10, 'K': 10, 'A': 11}

deck = deck.deck()
deck.shuffle()

playerhand = hand.hand(input('Ingrese el nombre de usuario que desea utilizar: '))
dealerhand = hand.hand('la casa')
dealerhand.add_new_card(deck.deal())
dealerhand.add_new_card(deck.deal())
dealerhand.printhand(True)
print('El valor de la mano de la casa es de: ', dealerhand.value)

print("")

playerhand.add_new_card(deck.deal())
playerhand.add_new_card(deck.deal())
playerhand.printhand()
print('El valor de la mano es de: ', playerhand.value)
# Se trae la función del modulo deck(deal) para que a dealerhand se le repartan las dos cartas.
# dealerhand.append(deck.deal())
# dealerhand.append(deck.deal())

# # Se llama a la función printhand del módulo utils para imprimir las cartas en pantalla. 
# utils.printhand('player 1', playerhand)
# print("")
# utils.printhand('Casa', dealerhand, True)
