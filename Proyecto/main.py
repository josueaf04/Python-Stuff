# Main page

import hand
import time
import os



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
        import deck
        wins = 0
        losses = 0

        import deck
        deck = deck.deck()
        deck.shuffle()
# Se determina si van a jugar 1 o 2 jugadores

        players = int(input('SELECCIONE 1 : 1 JUGADOR O 2 : 2 JUGADORES: \n'))
# Si el usuario selecciona 1 como respuesta se ejecuta la siguiente lógica

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
 # Si el usuario selecciona 'S' como opción se le entrega una nueva carta
                                
                                if choice == "s": 
                                        playerhand.add_new_card(deck.deal())
                                        playerhand.printhand()
                                        print(f'EL NUEVO VALOR DE LA MANO DE {username} ES: {playerhand.value}\n')
# Se le agrega la otra carta a la mano del dealer

                                        dealerhand.add_new_card(deck.deal())
                                        dealerhand.printhand()
                                        print(f'LA MANO DE LA CASA VALE: {dealerhand.value}\n')
# Si el usuario selecciona 'p' como opción se queda con la mano como la recibió y se le da la otra carta a la casa 
#      
                                elif choice == "p": 
                                        
                                        dealerhand.add_new_card(deck.deal())
                                        dealerhand.printhand()
                                        print(f'EL VALOR DE LA MANO DE LA CASA ES : {dealerhand.value}\n')
                                        playerhand.printhand()
                                        print(f'EL VALOR DE LA MANO DE {username} ES: {playerhand.value}\n')
                                        
                                        break
# Si el usuario selecciona 'a' como opción se termina el juego

                                elif choice == "a": 
                                        print(f'GRACIAS POR JUGAR {username}, VUELVE PRONTO')
                                        break    
# Si el usuario selecciona 1 como respuesta se ejecuta la siguiente lógica
                                                                                                       
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
# Se le plantean las opciones al primer usuario
                                
                                choice = input(f'{username} SELECCIONE LA ACCIÓN QUE DESEE TOMAR: [S]OLICITAR OTRA CARTA, [P]LANTARTE: \n')
                                clear()
                                print('FASE FINAL DEL JUEGO\n')
                                print(playerhand2.printhand[0])

                                
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
# Se le plantean las opciones al segundo usuario

                                choice2 = input(f'{username2} SELECCIONE LA ACCIÓN QUE DESEE TOMAR: [S]OLICITAR OTRA CARTA, [P]LANTARTE: \n') 

                                if choice2 == "s": 
                                        playerhand2.add_new_card(deck.deal())
                                        playerhand2.printhand()
                                        print(f'EL NUEVO VALOR DE LA MANO DE {username2} ES: {playerhand2.value}\n')                                            
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



        def play_again(): 
                repeat = (input('DESEA JUGAR[N]UEVA PARTIDA O [S]ALIR DEL JUEGO: ')).lower()
                while True:
                        if repeat == "n":
                                main()

                        elif repeat == "s":
                                print("GRACIAS POR JUGAR!")

                                break

         # Se ejecuta la lógica que determina al ganador

        while True:

                if dealerhand.value > 21: 
                        print(f"BLACKJACK! FELICIDADES {username} HAZ GANADO!")  
                        wins + 1
                        play_again()
                                
                if dealerhand.value == 21: 
                        losses + 1
                        print(f"BLACKJACK! LA CASA GANA!")
                        play_again()
                elif playerhand.value == 21: 
                        print(f"BLACKJACK! FELICIDADES {username} HAZ GANADO!")
                          
                        wins + 1
                        play_again()
                elif playerhand.value > 21: 
                        losses + 1
                        print(f"TE PASASTE! LA CASA GANA!")
                        play_again()
                elif dealerhand.value > 21: 
                        wins + 1 
                        print(f"{dealerhand} SE HA PASADO! FELICIDADES {username} HAZ GANADO! ")
                        play_again()
                elif 21 - dealerhand.value < 21 - playerhand.value: 
                        print("LA CASA GANA!")
                        losses + 1
                        play_again()
                elif 21 - playerhand.value < 21 - dealerhand.value:    
                        wins + 1 
                        
                        print(f"FELICIDADES {username}! HAZ GANADO!")
                        play_again()
                elif playerhand == dealerhand: 
                        print('EMPATE')  
                        play_again()

main()
