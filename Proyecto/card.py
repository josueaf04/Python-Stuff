# Clase del objeto carta
class card:
    
    def init(self, suit, rank): 
        self.rank = rank
        self.suit = suit

# Función que retorna el rango y el palo de carta

    def str(self): 
        return "" .join([self.rank, self.suit])
