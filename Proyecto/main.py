# Main page
<<<<<<< HEAD
=======
# Meter todo main en una función main
# Separar el código de main en funciones
>>>>>>> ecc01ad07ff2d50508c2fc07a5337f9bd00a18c4
import deck
import card
import hand
import time
import os
def clear(): 
        if os.name == 'nt': 
                os.system('CLS')
        if os.name == 'posiX': 
                os.system == ('clear')              

<<<<<<< HEAD

wins = 0
losses = 0


def game():
        global wins
        global losses
        choice = 0
        card.card.clear()

        print("\n    BIENVENIDO AL BLACKJACK!\n")
        print("-"*30+"\n")
        print("    \033[1;32;40mWINS:  \033[1;37;40m%s   \033[1;31;40mLOSSES:  \033[1;37;40m%s\n" % (wins, losses))
        print("-"*30+"\n")


        dealer_hand = card.card.deal(deck)
        player_hand = card.card.deal(deck)

        print ("EL REPARTIDOR TE MUESTRA UN " + str(dealer_hand[0]))
        print ("Tu tienes un " + str(player_hand) + " para un total de " + str(card.card.total(player_hand)))

        hand.Hand.blackjack(dealer_hand, player_hand)
        quit=False
        while not quit:
                choice = input("Que quieres [H]it, [S]tand, or [Q]uit: ").lower()
                if choice == 'h':
                        deck.deck.hit(player_hand)
                        print(player_hand)
                        print("El total del maso: " + str(card.card.total(player_hand)))
                if card.card.total(player_hand)>21:
                        print('Te pasaste')
                        losses += 1
                        deck.deck.play_again()
                elif choice=='s':
                        while card.card.total(dealer_hand)<17:
                                deck.deck.hit(dealer_hand)
                                print(dealer_hand)
                        if card.card.total(dealer_hand)>21:
                                print('Repartidor PERDIO!')
                                wins += 1
                                deck.deck.play_again()
                                hand.Hand.score(dealer_hand,player_hand)
                                deck.deck.play_again()
                        elif choice == "q":
                                print("Gracias  jugar!")
                                quit=True
                                exit()


                        if __name__ == "__main__":      
                                game()
=======
def main(): 
        import deck

# Stats
        wins = 0
        losses = 0

        print('BIENVENIDO A BLACKJACK\n')


        print("    \033[1;32;40mWINS:  \033[1;37;40m%s   \033[1;31;40mLOSSES:  \033[1;37;40m%s\n" % (wins, losses))

        players()

     
        
        
        
        
        

        # deck = deck.deck()
        # deck.shuffle()
# Se trae la clase hand del módulo hand y se asignan los nombres de los jugadores.

def players(): 
        import deck
        wins = 0
        losses = 0


        deck = deck.deck()
        deck.shuffle()

        players = int(input('SELECCIONE 1 : 1 JUGADOR O 2 : 2 JUGADORES: \n'))
        if players == 1: 
                        print('INGRESE EL USERNAME QUE DESEA UTILIZAR:  \n')
                        username = input()
                        playerhand = hand.hand(username)
                        dealerhand = hand.hand('LA CASA')
                        
                        print('INICIANDO LA PARTIDA... \n')
                        time.sleep(3)

                        dealerhand.add_new_card(deck.deal())
                        dealerhand.printhand()
                        print('* *')
                        print('LA MANO DE LA CASA VALE: *\n')
                        time.sleep(5)

                        playerhand.add_new_card(deck.deal())
                        playerhand.add_new_card(deck.deal())
                        playerhand.printhand()
                        print(f'LA MANO DE {username} VALE: {playerhand.value}\n')

                        while True:
                                
                                choice = input('SELECCIONE LA OPCION QUE DESEE: [S]OLICITAR OTRA CARTA, [P]LANTARTE, o [A]BANDONAR EL JUEGO: \n').lower()
                                clear()
                                print('FASE FINAL DEL JUEGO\n')
                # # Si el usuario seleccione 'S' como opción se le entrega una nueva carta
                                
                                if choice == "s": 
                                        playerhand.add_new_card(deck.deal())
                                        playerhand.printhand()
                                        print(f'EL NUEVO VALOR DE LA MANO DE {username} ES: {playerhand.value}\n')
                # # Se le agrega la otra carta a la mano del dealer

                                        dealerhand.add_new_card(deck.deal())
                                        dealerhand.printhand()
                                        print(f'LA MANO DE LA CASA VALE: {dealerhand.value}\n')
                                        
                                        
                                elif choice == "p": 
                                        
                                        dealerhand.add_new_card(deck.deal())
                                        dealerhand.printhand()
                                        print(f'EL VALOR DE LA MANO DE LA CASA ES : {dealerhand.value}\n')
                                        playerhand.printhand()
                                        print(f'EL VALOR DE LA MANO DE {username} ES: {playerhand.value}\n')
                                        
                                        break
                                elif choice == "a": 
                                        print(f'GRACIAS POR JUGAR {username}, VUELVE PRONTO')
                                        break    
                        # if dealerhand.value > 21: 
                        #         hand.values = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
                        #         'J': 10, 'Q': 10, 'K': 10,}         
                        if dealerhand.value == 21: 
                                losses + 1
                                print(f"BLACKJACK! LA CASA GANA!")
                        elif playerhand.value == 21: 
                                print(f"BLACKJACK! FELICIDADES {username} HAZ GANADO!")  
                                wins + 1
                        elif playerhand.value > 21: 
                                losses + 1
                                print(f"TE PASASTE! LA CASA GANA!")
                        elif dealerhand.value > 21: 
                                wins + 1 
                                print(f"{dealerhand} SE HA PASADO! FELICIDADES {username} HAZ GANADO! ")
                        elif 21 - dealerhand.value < 21 - playerhand.value: 
                                print("LA CASA GANA!")
                                losses + 1
                        elif 21 - playerhand.value < 21 - dealerhand.value:    
                                wins + 1 
                                print(f"FELICIDADES {username}! HAZ GANADO!")
                        elif playerhand == dealerhand: 
                                print('EMPATE')                                                                            
                
        elif players == 2: 
                        print('USUARIO 1, INGRESE EL USERNAME QUE DESEA UTILIZAR: \n') 
                        username = input()
                        print('USUARIO 2, INGRESE EL USERNAME QUE DESEA UTILIZAR: \n')
                        username2 = input()
                        playerhand = hand.hand(username)
                        playerhand2 = hand.hand(username2)
                        dealerhand = hand.hand('LA CASA')
                        print('INICIANDO LA PARTIDA... \n')
                        time.sleep(3)

                        dealerhand.add_new_card(deck.deal())
                        dealerhand.printhand()
                        print('* *')
                        print('LA MANO DE LA CASA VALE: *\n')
                        time.sleep(5)


                        playerhand.add_new_card(deck.deal())
                        playerhand.add_new_card(deck.deal())
                        playerhand.printhand()
                        print(f'LA MANO DE {username} VALE: {playerhand.value}\n')
                        time.sleep(5)
                        playerhand2.add_new_card(deck.deal())
                        playerhand2.add_new_card(deck.deal())
                        playerhand2.printhand()
                        print(f'LA MANO DE {username2} VALE: {playerhand2.value}\n') 

                        while True:
                                
                                choice = input(f'{username} SELECCIONE LA ACCIÓN QUE DESEE TOMAR: [S]OLICITAR OTRA CARTA, [P]LANTARTE: \n')
                                clear()
                                print('FASE FINAL DEL JUEGO\n')
                                print(playerhand2.printhand[0])
                                
                # # Si el usuario seleccione 'S' como opción se le entrega una nueva carta
                                
                                if choice == "s": 
                                        dealerhand.printhand()
                                        print(f'LA MANO DE LA CASA VALE: {dealerhand.value}\n')
                                        playerhand.add_new_card(deck.deal())
                                        playerhand.printhand()
                                        print(f'EL NUEVO VALOR DE LA MANO DE {username} ES: {playerhand.value[0]} \n')
                                elif choice == "p": 
                                        
                                        dealerhand.printhand()
                                        print(f'LA MANO DE LA CASA VALE: {dealerhand.value}\n')
                                        print(f'EL VALOR DE LA MANO DE LA CASA ES : {dealerhand.value}\n')
                                        playerhand.printhand()
                                        print(f'EL VALOR DE LA MANO DE {username} ES: {playerhand.value}\n')                                        
                          
                                else: 
                                        print('PORFAVOR ELIJA UNA OPCIÓN DE LAS LISTADAS')  

                                choice2 = input(f'{username2} SELECCIONE LA ACCIÓN QUE DESEE TOMAR: [S]OLICITAR OTRA CARTA, [P]LANTARTE: \n') 

                                if choice2 == "s": 
                                        playerhand2.add_new_card(deck.deal())
                                        playerhand2.printhand()
                                        print(f'EL NUEVO VALOR DE LA MANO DE {username2} ES: {playerhand2.value}\n')                                            
                # # Se le agrega la otra carta a la mano del dealer

                                        dealerhand.add_new_card(deck.deal())
                                        dealerhand.printhand()
                                        print(f'LA MANO DE LA CASA VALE: {dealerhand.value}\n')
                                        break 
                                elif choice2 == "p":
                        
                                        dealerhand.add_new_card(deck.deal())
                                        dealerhand.printhand()
                                        print(f'EL VALOR DE LA MANO DE LA CASA ES : {dealerhand.value}\n')
                                        playerhand.printhand()
                                        print(f'EL VALOR DE LA MANO DE {username2} ES: {playerhand2.value}\n')
                                        break
                        
                        
                        
        else: 
                        print("")
                        print(f'POR FAVOR SELECCIONE UNA DE LAS OPCIONES LISTADAS ANTERIORMENTE: \n')    
                             
                            

                        
# Se crea un loop para que el usuario indique qué acción desea tomar
                         

        # while True:
                                
        #         choice = input('SELECCIONE LA OPCION QUE DESEE: [S]OLICITAR OTRA CARTA, [P]LANTARTE, o [A]BANDONAR EL JUEGO: \n')
        #         print("")
        #         print('FASE FINAL DEL JUEGO\n')
        #         # # Si el usuario seleccione 'S' como opción se le entrega una nueva carta
                                
        #         if choice == 'S' or 's': 
        #                 playerhand.add_new_card(deck.deal())
        #                 playerhand.printhand()
        #                 print(f'EL NUEVO VALOR DE LA MANO DE {username} ES: {playerhand.value}\n')
        #         # # Se le agrega la otra carta a la mano del dealer

        #                 dealerhand.add_new_card(deck.deal())
        #                 dealerhand.printhand()
        #                 print(f'LA MANO DE LA CASA VALE: {dealerhand.value}\n')
        #                 break
                        
                                

main()
                                      
# Se ejecuta la lógica que determina al ganador

                        if dealerhand.value > 21: 
                                hand.values = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
                                'J': 10, 'Q': 10, 'K': 10,}         
                        print('El valor de la mano de La casa es de: ', dealerhand.value)
                        if dealerhand.value == 21: 
                                losses + 1
                                print(f"Blackjack! La casa gana!")
                        elif playerhand.value == 21: 
                                print(f"Blackjack! Felicidades {username} haz ganado!")  
                                wins + 1
                        elif playerhand.value > 21: 
                                losses + 1
                                print(f"Te pasaste! La casa gana!")
                        elif dealerhand.value > 21: 
                                wins + 1 
                                print(f"{dealerhand} se ha pasado! Felicidades {username}, haz ganado\! ")
                        elif 21 - dealerhand.value < 21 - playerhand.value: 
                                print(f"La casa gana!")
                                losses + 1
                        elif 21 - playerhand.value < 21 - dealerhand.value:    
                                wins + 1 
                                print(f"Felicidades {username}! Haz ganado\!") 
# Si el usuario selecciona 'P' como su opción, se queda con la mano actual y se le agrega la faltante a la casa
                
#                 elif choice == 'P':

#                         dealerhand.add_new_card(deck.deal())
#                         dealerhand.printhand()
#                         print(f'El valor de la mano de la casa es: {dealerhand.value}')
#                         if dealerhand.value == 21: 
#                                 losses + 1
#                                 print(f"Blackjack! La casa gana!")
#                         elif playerhand.value == 21: 
#                                 print(f"Blackjack! Felicidades {username} haz ganado!")  
#                                 wins + 1
#                         elif playerhand.value > 21: 
#                                 losses + 1
#                                 print(f"Te pasaste! La casa gana!")
#                         elif dealerhand.value > 21: 
#                                 wins + 1 
#                                 print(f"{dealerhand} se ha pasado! Felicidades {username}, haz ganado\! ")
#                         elif 21 - dealerhand.value < 21 - playerhand.value: 
#                                 print(f"La casa gana!")
#                                 losses + 1
#                         elif 21 - playerhand.value < 21 - dealerhand.value:    
#                                 wins + 1 
#                                 print(f"Felicidades {username}! Haz ganado!")
# # Finalmenmte si el usuario selecciona 'A' como su opción, el juego se termina

#                 elif choice == 'A':
#                         print('Gracias por jugar, vuelve pronto!\n')
#                         break
# # Si el usuario selecciona una opción no listada, se le solicita que ingrese una opción listada
#                 else: 
#                         print('Por favor escriba una de las opciones listadas: [S]olicitar, [P]lantarte, o [A]bandonar el juego:')
# main()                
>>>>>>> ecc01ad07ff2d50508c2fc07a5337f9bd00a18c4
