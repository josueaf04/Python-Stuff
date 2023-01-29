"Elimina repetidos"

# Problema: Crear un programa que elimine los digitos repetidos de una lista e imprima una nueva sin ellos.

# La interfaz del programa será la consola de comando, el programa recibirá una lista, analizará si dicha lista contiene digitos iguales,
# si los hay, creará una nueva lista sin ellos.

# Pseudocódigo:
# El programa recibe la lista.
# Procesa dicha lista en un set, cuya función es eliminar los digitos iguales.
# Crea una lista vacía "output". 
# Se genera un loop "for" con variable "i" para iterar sobre nuestro set.
# Con el loop ya creado mediante append() se agrega a la lista vacía la variable "i".
# Finalmente se imprime la lista "output".

# Subproblemas: Crear el set, generar la lista vacía en la que se imprimirá nuestro output, por otro lado desarrollar el loop for,
# agregar la variable de nuestro loop a la lista vacía, que el programa imprima la lista sin los digitos repetidos.

# Resolución: 

list = [1, 2, 3, 3, 2, 4, 6]
eliminar = set(list)
output = [] 
for i in eliminar: 
    output.append(i) 
print(output)

list = [3, 3 , 3, 3, 3, 3, 3]
eliminar = set(list)
output = [] 
for i in eliminar: 
    output.append(i) 
print(output)