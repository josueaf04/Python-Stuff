# Main page

import deck
import hand
# Se mezcla el deck

deck = deck.deck()
deck.shuffle()

# Se trae la clase hand del módulo hand y se asignan los nombres de los jugadores.
playerhand = hand.hand(input('Ingrese el nombre de usuario que desea utilizar: '))
dealerhand = hand.hand('La casa')
# Se le agregan dos cartas a "dealerhand"

dealerhand.add_new_card(deck.deal())
dealerhand.add_new_card(deck.deal())
dealerhand.printhand(True)
print('El valor de la mano de La casa es de: ', dealerhand.value)

print("")
# Se le agregan dos cartas a "playerhand"

playerhand.add_new_card(deck.deal())
playerhand.add_new_card(deck.deal())
playerhand.printhand()
print('El valor de la mano es de: ', playerhand.value)

if dealerhand.value == 21: 
    print(f"Blackjack!{dealerhand} gana!")
elif playerhand.value == 21: 
    print(f"Blackjack! Felicidades josue haz ganado!")  
elif playerhand.value > 21: 
    print(f"Te pasaste! {dealerhand} gana!")
elif dealerhand.value > 21: 
    print(f"{dealerhand} se ha pasado! Felicidades josue, haz ganado! ") 
elif 21 - dealerhand.value < 21 - playerhand.value: 
    print(f"{dealerhand} gana!")
elif 21 - playerhand.value < 21 - dealerhand.value:    
    print(f"Felicidades josue! Haz ganado!")     

