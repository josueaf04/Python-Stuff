# Main page
# Meter todo main en una función main
# Separar el código de main en funciones
import deck
import hand
import time
import os
import utils


def clear(): 
        if os.name == 'nt': 
                os.system('CLS')
        if os.name == 'posix': 
                os.system('clear')         

def main(): 
        

# Stats
        wins = 0
        losses = 0

        print('BIENVENIDO A BLACKJACK\n')


        print("    \033[1;32;40mWINS:  \033[1;37;40m%s   \033[1;31;40mLOSSES:  \033[1;37;40m%s\n" % (wins, losses))

        players()

       



       



# Se trae la clase hand del módulo hand y se asignan los nombres de los jugadores.

def players(): 
       
        wins = 0
        losses = 0


        # deck = deck.deck()
        # deck.shuffle()

        players = int(input('SELECCIONE 1 : 1 JUGADOR O 2 : 2 JUGADORES: \n'))
        if players == 1: 
                        print('INGRESE EL USERNAME QUE DESEA UTILIZAR:  \n')
                        username = input()
                        playerhand = hand.hand(username)
                        dealerhand = hand.hand('LA CASA')
                        
                        print('INICIANDO LA PARTIDA... \n')
                        time.sleep(3)

                        dealerhand.add_new_card(deck.())
                        dealerhand.printhand()
                        print('* *')
                        print('LA MANO DE LA CASA VALE: *\n')
                        time.sleep(5)

                        deck.deck.deal

                        playerhand.add_new_card(deck.deck.deal())
                        playerhand.add_new_card(deck.deck.deal())
                        playerhand.printhand()
                        print(f'LA MANO DE {username} VALE: {playerhand.value}\n')

                        while True:
                                
                                choice = input('SELECCIONE LA OPCION QUE DESEE: [S]OLICITAR OTRA CARTA, [P]LANTARTE, o [A]BANDONAR EL JUEGO: \n').lower()
                                clear()
                                print('FASE FINAL DEL JUEGO\n')
                # # Si el usuario seleccione 'S' como opción se le entrega una nueva carta
                                
                                if choice == "s": 
                                        playerhand.add_new_card(deck.deck.deal())
                                        playerhand.printhand()
                                        print(f'EL NUEVO VALOR DE LA MANO DE {username} ES: {playerhand.value}\n')
                # # Se le agrega la otra carta a la mano del dealer

                                        dealerhand.add_new_card(deck.deck.deal())
                                        dealerhand.printhand()
                                        print(f'LA MANO DE LA CASA VALE: {dealerhand.value}\n')
                                        
                                        
                                elif choice == "p": 
                                        
                                        dealerhand.add_new_card(deck.deck.deal())
                                        dealerhand.printhand()
                                        print(f'EL VALOR DE LA MANO DE LA CASA ES : {dealerhand.value}\n')
                                        playerhand.printhand()
                                        print(f'EL VALOR DE LA MANO DE {username} ES: {playerhand.value}\n')
                                        
                                        break
                                elif choice == "a": 
                                        print(f'GRACIAS POR JUGAR {username}, VUELVE PRONTO')
                                        break    
                                                                                                    
                
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

                        dealerhand.add_new_card(deck.deck.deal())
                        dealerhand.printhand()
                        print('* *')
                        print('LA MANO DE LA CASA VALE: *\n')
                        time.sleep(5)


                        playerhand.add_new_card(deck.deck.deal())
                        playerhand.add_new_card(deck.deck.deal())
                        playerhand.printhand()
                        print(f'LA MANO DE {username} VALE: {playerhand.value}\n')
                        time.sleep(5)
                        playerhand2.add_new_card(deck.deck.deal())
                        playerhand2.add_new_card(deck.deck.deal())
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
                                        playerhand.add_new_card(deck.deck.deal())
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
                                        playerhand2.add_new_card(deck.deck.deal())
                                        playerhand2.printhand()
                                        print(f'EL NUEVO VALOR DE LA MANO DE {username2} ES: {playerhand2.value}\n')                                            
                # # Se le agrega la otra carta a la mano del dealer

                                        dealerhand.add_new_card(deck.deck.deal())
                                        dealerhand.printhand()
                                        print(f'LA MANO DE LA CASA VALE: {dealerhand.value}\n')
                                        break 
                                elif choice2 == "p":
                        
                                        dealerhand.add_new_card(deck.deck.deal())
                                        dealerhand.printhand()
                                        print(f'EL VALOR DE LA MANO DE LA CASA ES : {dealerhand.value}\n')
                                        playerhand.printhand()
                                        print(f'EL VALOR DE LA MANO DE {username2} ES: {playerhand2.value}\n')
                                        break
                        
                        
                        
        else: 
                        print("")
                        print(f'POR FAVOR SELECCIONE UNA DE LAS OPCIONES LISTADAS ANTERIORMENTE: \n') 

         # Se ejecuta la lógica que determina al ganador

        while True:

                if dealerhand.value > 21: 
                        print(f"BLACKJACK! FELICIDADES {username} HAZ GANADO!")  
                        wins + 1
                        utils.playagain()
                                
                if dealerhand.value == 21: 
                        losses + 1
                        print(f"BLACKJACK! LA CASA GANA!")
                        utils.playagain()
                elif playerhand.value == 21: 
                        print(f"BLACKJACK! FELICIDADES {username} HAZ GANADO!")
                        utils.playagain()  
                        wins + 1
                elif playerhand.value > 21: 
                        losses + 1
                        print(f"TE PASASTE! LA CASA GANA!")
                        utils.playagain()
                elif dealerhand.value > 21: 
                        wins + 1 
                        print(f"{dealerhand} SE HA PASADO! FELICIDADES {username} HAZ GANADO! ")
                        utils.playagain()
                elif 21 - dealerhand.value < 21 - playerhand.value: 
                        print("LA CASA GANA!")
                        losses + 1
                        utils.playagain()
                elif 21 - playerhand.value < 21 - dealerhand.value:    
                        wins + 1 
                        print(f"FELICIDADES {username}! HAZ GANADO!")
                        utils.playagain()
                elif playerhand == dealerhand: 
                        print('EMPATE')  
                        utils.playagain() 
                             
                            

                        

                        
                                

main()

 



                                      

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