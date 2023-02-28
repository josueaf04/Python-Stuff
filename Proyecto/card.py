# Clase del objeto carta

class card: 
    def __init__(self, suit, rank): 
        self.rank = rank
        self.suit = suit

    def __str__(self): 
        return "" .join(self.rank, self.suit)
            
