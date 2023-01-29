"Notas de clase"

# Crear un programa que saque el promedio de las notas dadas y que ese promedio se imprima en un diccionario.

# La interfaz del programa será la consola de comando, el programa hará el cálculo del promedio de las notas y creará un diccionario con el nombre del estudiante
# y su promedio calculado.

# Pseudocódigo: 
# El programa recibe las notas, las cuáles van en variable separadas para evitar la formación de una tupla.
# Ya creadas las variables, se crea una para hacer la unión de las 3 anteriores.
# Se desarrolla una variable "n" con la cantidad de notas que fueron ingresadas.
# El programa crea una variable int() en la que se hace el cálculo de las notas entre la cantidad de notas a calcular. 
# Finalmente se genera un diccionario con formato {nombre : promedio}. 

#Subproblemas: 
# Crear las variables con el valor de las notas, unir esos valores en una variable nueva, generar la variable que contenga la cantidad de notas a calcular, unir
# estas dos y dividirlas para sacar el promedio, desarrollar el diccionario. 

# Resolución: 

physics = 70
history = 80
math = 90
marks = physics + history + math 
n = 3 
prom = int(marks / n)
print("La nota promedio del estudiante es", prom)
nota_promedio = {"Estudiante: Mike, Nota Promedio: 80"}
print(nota_promedio)