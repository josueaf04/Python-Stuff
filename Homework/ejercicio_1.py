"Factorial del numero dado"

# Problema: Crear un programa que dé como resultado el factorial del número ingresado por el usuario (input).

# Planeación: La interfaz del programa será la consola de comando, su función dar como resultado el factorial del número ingresado por el usuario.

# Pseudocódigo: 
# El usuario ingresa un número entero al programa.
# Utilizando una validación if / else, el programa valida el input hecho por el usuario.
# El programa genera un loop que va desde 1 y termina en el input.
# La variable "factorial" se multiplica por cada uno de los números contenidos en el loop.
# Imprimiendo como resultado final el factorial del input.

# Subproblemas: 
# Crear la variable "num" para el input del usuario.
# Generar la validación if / else para comprobar si el número ingresado se puede procesar.
# Desarrollar la variable "factorial".
# Crear un loop "for _ in range" para multiplicar "factorial" * los números contenidos en el loop.
# El programa debe imprimir el factorial correcto.

num = int(input("Ingrese un número mayor a 0: ")) 
if num > 0: 
    print("") 
else: 
    print("Error, el número ingresado debe ser mayor a 0")   
factorial = 1
for i in range(1, num + 1): 
    factorial *= i 
print("El factorial de su número es", factorial) 
  
