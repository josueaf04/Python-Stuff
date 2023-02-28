import random
dealerIn = True 
playerIn = True 

#Deck & hands
deck_of_cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10,
                 'J', 'Q', 'k', 'A', 'J', 'Q', 'k', 'A', 'J', 'Q', 'k', 'A', 'J', 'Q', 'k', 'A']
dealer_hand = []
player_hand = []

# Deal the cards

def deal_cards(turn): 
    card = random.choice(deck_of_cards)          
    turn.append(card)  
    deck_of_cards.remove(card)
    
# Calculate the total of each hand
def total(turn): 
   total = 0  
   face_cards = ['J', 'Q', 'K']
   ace_11s = 0 
   for card in turn: 
        if card in range(1, 11): 
           total += card
        elif card in face_cards: 
           total += 10 
        else: 
            total += 11
            ace_11s += 1
        while ace_11s and total > 21:
            total -= 10
            ace_11s -= 1
   return total    

# Check for the winner 
def revealDealersHand(): 
    if len(dealer_hand) == 2: 
        return dealer_hand[0]
    elif len(dealer_hand) > 2: 
        return dealer_hand[0], dealer_hand[1]

# Game loop 
for _ in range(2): 
    deal_cards(dealer_hand)
    deal_cards(player_hand)

while playerIn or dealerIn: 
    print("Ingrese su username: ")
    username = input(str())
    print(f"La casa tiene: {revealDealersHand()} y *") 
    print(f"Tú tienes {player_hand}, el total de tu mazo es de {total(player_hand)}")
    if playerIn: 
        stayOhit = input("s: Para quedarte con el mazo como está\nt: Para pedir una carta extra\n")
    if stayOhit == 's': 
        playerIn = False
    else: 
        deal_cards(player_hand)        
    if dealer_hand > 16: 
        dealerIn = False 
    else: 
        deal_cards(dealer_hand)
    if total(player_hand) >= 21: 
        break 
    elif total(dealer_hand) >= 21: 
        break 

if total(player_hand) == 21: 
    print(f"\nTú tienes {player_hand}, el total de tu mazo es de: 21, mientras que la casa tiene {dealer_hand}, con un total de {total(dealer_hand)}")
    print(f"Blackjack!\nFelicidades {username} haz ganado!!")
elif total(dealer_hand) == 21: 
    print(f"\nTú tienes {player_hand}, el total de tu mazo es de: {total(player_hand)}, mientras que la casa tiene {dealer_hand}, con un total de {total(dealer_hand)}") 
    print("Blackjack! La casa gana!!")    
elif total(player_hand) > 21: 
    print(f"\nTú tienes {player_hand}, el total de tu mazo es de: {total(player_hand)}, mientras que la casa tiene {dealer_hand}, con un total de {total(dealer_hand)}")
    print("Te pasaste! La casa gana!!") 
elif total(dealer_hand) > 21: 
    print(f"\nTú tienes {player_hand}, el total de tu mazo es de: {total(player_hand)}, mientras que la casa tiene {dealer_hand}, con un total de {total(dealer_hand)}")
    print(f"El dealer se ha pasado! Felicidades {username} haz ganado") 
elif 21 - total(dealer_hand) < 21 - total(player_hand): 
    print(f"\nTú tienes {player_hand}, el total de tu mazo es de: {total(player_hand)}, mientras que la casa tiene {dealer_hand}, con un total de {total(dealer_hand)}") 
    print("La casa gana!") 
elif 21 - total(dealer_hand) > 21 - total(player_hand): 
    print(f"\nTú tienes {player_hand}, el total de tu mazo es de: {total(player_hand)}, mientras que la casa tiene {dealer_hand}, con un total de {total(dealer_hand)}") 
    print(f"Felicidades {username} haz ganado!")
                