***Autores***:  Andy Foster Morgan y Josué Angulo Frino

***Nombre del proyecto:*** *Proyecto Blackjack.*

## ***Descripción del proyecto***

El proyecto consiste en la creación de un programa o aplicación que tenga la funcionalidad del juego de cartas "blackjack" o "21",  dicha aplicación tendrá entre sus funcionalidades: el iniciar una partida, repartir las cartas a la casa y al usuario, pedir cartas, determinar el ganador, entre muchas otras. 

## *Diseño de la solución*

Teniendo en cuenta el problema("ya descrito arriba"), planeamos lo siguiente: Dividir nuestro programa en módulos, cuyo contenido serán las clases de los objetos necesarios y otro contendrá nuestro "main page", en el main page decidimos estructurar todo el código relacionado a la lógica del juego, el pedir otra carta por ejemplo. Teniendo esta planeación en cuenta identificamos "subproblemas", algunos como: Crear las inputs del usuario, crear los módulos, las clases y la lógica del juego, entre muchos otros. 
Distribución del código: 
Módulo "card": Contiene la clase card, la funcionalidad de esta clase es representar una carta, con los parámetros suit y rank, y retornar una string que con esos parámetros. 
Módulo "deck": Presenta las constantes "suits" y "ranks". Contiene la clase deck, su función es la de mezclar, repartir y retornar las cartas. 
Módulo "hand": Presenta la constante "values". Contiene la clase hand, cuya función es añadir las cartas a las manos e imprimir las cartas.



## ***Manual de usuario***

 print(hola)



## *Consideraciones especiales*