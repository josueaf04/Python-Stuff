# Clase del objeto hand
import main
import card
import utils
import deck



class Hand:
    def blackjack(dealer_hand, player_hand):
        (main.wins)
        (main.losses)
        if card.card.total(player_hand) == 21:
            utils.utils.print_results(dealer_hand, player_hand)
            print ("Felicitaciones! Tu tienes un Blackjack!\n")
            main.wins += 1
            deck.deck.play_again()
        elif card.card.total(dealer_hand) == 21:
            utils.utils.print_results(dealer_hand, player_hand)
            print ("Perdon, perdiste. el repartidor tiene un blackjack.\n")
            main.losses += 1
            deck.deck.play_again()

    def score(dealer_hand, player_hand):
        (main.wins) 
        (main.losses)

<<<<<<< HEAD
        if card.card.total(player_hand) == 21:
            utils.utils.print_results(dealer_hand, player_hand)
            print ("Felicitaciones! Tu tienes un Blackjack!\n")
            main.wins += 1
        elif card.card.total(dealer_hand) == 21:
            utils.utils.print_results(dealer_hand, player_hand)
            print ("Perdon, perdiste. el repartidor tiene un blackjack.\n")
            main.losses += 1
        elif card.card.total(player_hand) > 21:
            utils.utils.print_results(dealer_hand, player_hand)
            print ("Perdon, perdiste.\n")
            main.losses += 1
        elif card.card.total(dealer_hand) > 21:
            utils.utils.print_results(dealer_hand, player_hand)
            print ("Felicitaciones! GANASTE!\n")
            main.wins += 1
        elif card.card.total(player_hand) < card.card.total(dealer_hand):
            utils.utils.print_results(dealer_hand, player_hand)
            print (" Tu resultado es menor al del repartidor. PERDISTE!\n")
            main.losses += 1
        elif card.card.total(player_hand) > card.card.total(dealer_hand):
            utils.utils.print_results(dealer_hand, player_hand)
            print ("Felicitaciones! Tu puntaje es mayor al del repartidor. GANASTE!\n")
            main.wins += 1
        
=======
    def printhand(self): 
        print(f'LA MANO DE {self.playername} ES: \n')
        for i in range(0, len(self.cardlist)): 
            print(self.cardlist[i].__str__(),'\n')
# Función que añade la carta con su respectivo valor.

    def add_new_card(self, card): 
        self.cardlist.append(card)
        self.value += values[card.rank]
    
    
>>>>>>> ecc01ad07ff2d50508c2fc07a5337f9bd00a18c4
