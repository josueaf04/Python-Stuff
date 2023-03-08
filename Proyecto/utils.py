# Módulo con funciones útiles

import main

class playagain:
        def play_again(): 
                repeat = (input('Desea jugar[N]ueva partida o [S]alir del juego: ')).lower()

                if repeat == "n":
                        main.players()

                elif repeat == "s":
                        print("Gracias por jugar!")
