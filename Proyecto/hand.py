# Clase del objeto hand

values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
          'J': 10, 'Q': 10, 'K': 10, 'A': 11}

class hand: 
    def __init__(self, playername): 
        self.playername = playername
        self.cardlist = []
        self.value = 0 

    def printhand(self, isdealer = False): 
        print(f'La mano de {self.playername} es: \n')
        for i in range(0, len(self.cardlist)): 
            if isdealer and i == 0: 
                print('* *')
            else: 
                print(self.cardlist[i].__str__(),'\n')

    def add_new_card(self, card): 
        self.cardlist.append(card)
        self.value += values[card.rank]