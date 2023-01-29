"Lista al cubo"

# Problema: Crear un programa que eleve los digitos de una lista al cubo, en una nueva lista.

# Planeación: La interfaz del programa será la consola de comando, el programa recibirá una lista con ciertos numeros, el output deseado es que el programa cree una
# nueva lista pero con el resultado del cubo de estos numeros. 

# Pseudocódigo: 
# El programa recibe una lista con numeros.
# Crea una lista vacía en la cuál irá el output que se busca.
# Se genera un loop "for" con variable "num" para iterar sobre la lista con los numeros.
# Cada vez que num pase por "list" eleva los valores al cubo.
# Utilizando append() se agrega la variable "num" a la lista vacía.
# Imprime el output. 

# Subproblemas: Crear la lista vacía, desarrollar el loop for para iterar sobre la lista con los numeros, dentro de ese loop elevar la variable al cubo, 
# añadir la variable a la lista vacía e imprimir.

# Resolución: 

list = [1, 2, 3]
output = []
for num in list: 
    num **= 3 
    output.append(num)
print(output) 
