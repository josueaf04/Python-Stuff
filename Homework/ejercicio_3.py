"Strings intercaladas"

# Problema: Crear un programa que reciba dos palabras del mismo largo y que cree una nueva con los caracteres intercalados. 

# La interfaz del programa será la consola de comando, la función del programa será recibir dos palabras del mismo largo y crear
# una string con los caracteres de esas palabras intercalados.

# Pseudocódigo: 
# Se crean 2 inputs para que el usuario ingrese las 2 palabras.
# Mediante una validación "if" el programa analiza si las palabras contienen el mismo número de caracteres.
# Genera una variable en la cual se concatenan los dos inputs.

# Subproblemas: Crear las variables en las que estarán los inputs, crear la validación "if", concatenar los inputs en una variable nueva.

str = input("Ingrese una palabra: ")
str2 = input("Ingrese otra palabra que contenga los mismos digitos que la anterior: ")
if len(str) != len(str2): 
    print("Error, las palabras deben de tener el mismo número de digitos.")
x = [str + str2] 




