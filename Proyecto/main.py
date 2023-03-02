# Main page

import deck
import hand
# Se mezcla el deck

deck = deck.deck()
deck.shuffle()

# Se trae la clase hand del módulo hand y se asignan los nombres de los jugadores.
playerhand = hand.hand(input('Ingrese el nombre de usuario que desea utilizar: '))
dealerhand = hand.hand('la casa')
# Se le agregan dos cartas a "dealerhand"

dealerhand.add_new_card(deck.deal())
dealerhand.add_new_card(deck.deal())
dealerhand.printhand(True)
print('El valor de la mano de la casa es de: ', dealerhand.value)

print("")
# Se le agregan dos cartas a "playerhand"

playerhand.add_new_card(deck.deal())
playerhand.add_new_card(deck.deal())
playerhand.printhand()
print('El valor de la mano es de: ', playerhand.value)