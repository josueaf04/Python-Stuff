# Main page

import deck
import hand

wins = 0
losses = 0

# Se mezcla el deck
print('Bienvenido a Blackjack\n')
# print('1 : 1 Jugador / 2 : 2 Jugadores')

print("    \033[1;32;40mWINS:  \033[1;37;40m%s   \033[1;31;40mLOSSES:  \033[1;37;40m%s\n" % (wins, losses))

# players = int(input())

deck = deck.deck()
deck.shuffle()

# Se trae la clase hand del módulo hand y se asignan los nombres de los jugadores.
print('Ingrese el username que desea utilizar')
username = input()
print("")
playerhand = hand.hand(username)
dealerhand = hand.hand('La casa')
# Se le agregan dos cartas a "dealerhand"

dealerhand.add_new_card(deck.deal())
dealerhand.add_new_card(deck.deal())
dealerhand.printhand(True)
if dealerhand.value > 21: 
        hand.values = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
          'J': 10, 'Q': 10, 'K': 10,}
print('El valor de la mano de La casa es de: ', dealerhand.value)
 
print("")
    # Se le agregan dos cartas a "playerhand"

playerhand.add_new_card(deck.deal())
playerhand.add_new_card(deck.deal())
playerhand.printhand()

print('El valor de tu mano es de: ', playerhand.value)

if dealerhand.value == 21: 
        print(f"Blackjack! La casa gana!")
        losses + 1
elif playerhand.value == 21: 
        print(f"Blackjack! Felicidades {username} haz ganado!")  
        wins + 1
elif playerhand.value > 21: 
        print(f"Te pasaste! La casa gana!")
        losses + 1
elif dealerhand.value > 21: 
        print(f"{dealerhand} se ha pasado! Felicidades {username}, haz ganado! ")
        wins + 1 
elif 21 - dealerhand.value < 21 - playerhand.value: 
        print(f"La casa gana!")
        losses + 1
elif 21 - playerhand.value < 21 - dealerhand.value:    
        print(f"Felicidades {username}! Haz ganado!")
        wins + 1 
elif playerhand.value == dealerhand.value: 
        print('Empate!')        

while not quit: 
        choice = input('Selecciona la opción que desees: [H]it, [S]tand, or [Q]uit: ')
        if choice == 'H' or 'h': 
                playerhand.add_new_card(deck.deal())
                playerhand.printhand()
                if playerhand.value > 21: 
                    hand.values = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
                    'J': 10, 'Q': 10, 'K': 10,}
                print('El nuevo valor de tu mano es de: ', playerhand.value) 

                if dealerhand.value == 21: 
                            print(f"Blackjack! La casa gana!")
                            losses + 1
                elif playerhand.value == 21: 
                        print(f"Blackjack! Felicidades {username} haz ganado!")  
                        wins + 1
                elif playerhand.value > 21: 
                        print(f"Te pasaste! La casa gana!")
                        losses + 1
                elif dealerhand.value > 21: 
                        print(f"{dealerhand} se ha pasado! Felicidades {username}, haz ganado! ")
                        wins + 1 
                elif 21 - dealerhand.value < 21 - playerhand.value: 
                        print(f"La casa gana!")
                        losses + 1
                elif 21 - playerhand.value < 21 - dealerhand.value:    
                        print(f"Felicidades {username}! Haz ganado!")
                        wins + 1 