# Clase del objeto carta

class card: 
#Función inicializadora 

    def __init__(self, suit, rank): 
        self.rank = rank
        self.suit = suit
# Función que retorna el rango y el palo de carta

    def __str__(self): 
        return "" .join([self.rank, self.suit])
    