# Módulo con funciones útiles
import main 
import card


class utils:
    def print_results(dealer_hand, player_hand):
            card.card.clear()

            print("\n    BIENVENIDO AL BLACKJACK!\n")
            print("-"*30+"\n")
            print("    \033[1;32;40mWINS:  \033[1;37;40m%s   \033[1;31;40mLOSSES:  \033[1;37;40m%s\n" % (main.wins, main.losses))
            print("-"*30+"\n")
            print ("EL REPARTIDOR TE MUESTRA UN: " + str(dealer_hand) + " Para un total de. " + str(card.card.total(dealer_hand)))
            print ("Tu tienes un " + str(player_hand) + " para un total de: " + str(card.card.total(player_hand)))


 

    


