"Triangulo"

# Problema: Crear un programa cuyo output genere un patrón en forma de triángulo que finalice al llegar al input.

# Planeación: La interfaz del programa será la consola de comando, la función del programa será crear un patrón en forma de triángulo
# finalizando este en el número que el usuario ingresó.

#Pseudocódigo
# El usuario ingresa un número mayor a 0.
# Mediante una validación de if / else, el programa comprueba si ese input es mayor a 0, si no lo es imprime "Error"
# El programa genera un loop que empieza en 1 y termina en el input.
# Imprime "" para que cada vez que "i" se itera, sea en una línea distinta (hacia abajo).
# Luego el programa crea un loop (dentro del loop ya existente) que va desde 1 hasta la variable "i".
# Finalmente imprime "j" y declara que ese loop termina en " " para evitar que los números de "j" se ejecuten
# sin espacio 


num = int(input("Ingrese un número mayor a 0: ")) 
if num > 0: 
    print("")
else: 
    print("Error, el número ingresado debe ser mayor a 0")    
for i in range(1, num + 1): 
    print("")
    for j in range (1, i+ 1): 
        print(j, end = " ") 