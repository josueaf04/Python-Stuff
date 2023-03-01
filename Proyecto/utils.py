# Módulo con funciones útiles

def printhand(player, hand, isdealer = False): 
    print(f'La mano de {player} es: \n')
    for i in range(0, len(hand)): 
        if isdealer and i == 0: 
            print('* *')
        else: 
            print(hand[i].__str__())            