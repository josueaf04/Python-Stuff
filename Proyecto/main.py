# Main page
import deck
import card
import hand


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