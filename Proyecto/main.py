# Main page

import deck
import hand

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

