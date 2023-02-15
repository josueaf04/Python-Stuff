# Ejercicio 1 (función que cuenta e imprime en pantalla todos los números, letras y caracteres especiales)

# Problema: Crear una función que cuente e imprima en pantlla los números, letras y caracteres especiales que reciba como parámetro.

# Planeación: Mediante la consola de comandos, usando la función creada el programa contará e imprimirá los números, letras y caracteres especiales.

# Pseudocódigo: 
# Se crea la función que recibirá el parámetro "str"
# La funcionalidad de la función comienza con 3 variables = 0 
# Se crea un ciclo for  para iterar sobre str 
# Dentro del loop for se valida cada iteración utilizando un condicional if, para determinar si es un número(isnumeric()), una letra(isalpha()) 
# o caracter especial (mediante descarte con un else)
# A las variables = 0 se les suma 1 para que así se cuente la cantidad de caracteres que hay de ese tipo.
# Finalmente se imprimen los resultados

# Subproblemas: Crear la función, dentro de ella crear las variables, el ciclo for, la validación para determinar qué tipo de caracter es cada iteración, 
# sumar 1 a las variables = 0, finalmente que se impriman los resultados.


def contar_caracteres(str): 

    num = 0
    let = 0
    espe= 0

    for i in str: 
        if i.isnumeric(): 
            num += 1     
        elif i.isalpha(): 
            let += 1   
        else: 
            espe += 1

    print("Números: ", num) 
    print("Letras: ", let) 
    print("Caracteres especiales: ", espe)  

test = contar_caracteres("pppp22222]]]]]")
print("")
test_2 = contar_caracteres("juicewrld999/////")
print("")
test_3 = contar_caracteres("Mi nombre es Josue,2004,,,,")
print("")
test_4 = contar_caracteres("")
print("")
        

# Ejercicio 2 (función que cuenta todas las apariciones de cada caracter en una string)    

# Problema: Crear una función que cuente todas las apariciones de cada caracter en una string e imprima el resultado en un diccionario

# Planeación: Mediante la consola de comandos, usando la función creada el programa contará las apariciones de cada caracter e imprimirá el resultado en un diccionario.

# Pseudocódigo: 
# Se crea la función que recibirá el parámetro str
# Dentro de esta se generan dos variables vacías, una = 0 y otra que contiene un diccionario vacío 
# Se crea un loop for para iterar sobre str
# Se genera un condicional if con el método keys() 
# En caso de que la iteración ya esté contenida en el diccionario se le suma uno, al igual que a la variable = 0
# Si no lo está mediante un else se agrega la iteración al diccionario y de igual forma se le suma 1 a la variable = 0, la cuál lleva el conteo de apariciones
# Finalmente se imprime en pantalla el diccionario.

# Subproblemas: Crear la función, dentro de ella crear la variable y el diccionario vacíos, crear el loop for, agregar el condicional if y el metodo keys(), 
# si i ya está en el diccionario que se le sume uno, al igual que a la variable = 0, si no lo está que se agregue y se le sume 1 a la variable = 0, finalmente
# imprimir en pantalla el diccionario con los datos.

def contar_apariciones(str): 
    
    counter = 0
    apa = {} 

    for i in str: 
        
        if i in apa.keys(): 
                apa[i] += 1
                counter += 1      
        else: 
            apa[i] = 1  
            counter += 1
 
    print(apa)

test = contar_apariciones("SanValentín")
print("")
test_2 = contar_apariciones("")
print("")
test_3 = contar_apariciones("9044882004")
print("") 
test_4 = contar_apariciones("'''''¿¿¿¿¿¿?????")
print("")


# Ejercicio 3 (función que elimina todas las apariciones de un elemento en una lista)   

def eliminar_valor(list): 
    valor = 0
    list = [20, 30, 40, 20, 5, 100, 5, 20] 

    for i in list: 
        valor += 1
        count = list.count(i)

        if count >= 2: 
            list.remove(i)
            
    print(list)

eliminar_valor(list)

 
# print(eliminar_valor(list))

# Ejercicio 4 (función que recibe una secuencia de números separados por coma por parte del usuario e 
# imprima una lista y una tupla que contengan dichos valores)

# Problema: Crear una función que reciba una secuencia de números como input e imprima dichos valores en una lista y una tupla. 

# Planeación: Mediante la consola de comando, la función creada imprimirá el input recibido en una lista y una tupla.

# Pseudocódigo: 
# Se crea la función
# Dentro de ella se genera un loop for y un condicional if para iterar sobre el input
# En el if se crea una lista vacía y mediante el método append se le agrega el input
# Luego se crea una tupla vacía, luego se convierte a lista para agregarle el input mediante .append, 
# Finalmente se crea otra tupla que es = a la lista que contiene el input y se le suma a la tupla vacía del inicio y se imprime el resultado de la función.

# Subproblemas: Crear la función, dentro de ella generar el loop for y la validación if, en él generar la lista vacía y agregarle el input, también agregar
# la tupla vacía, convertirla en lista, agregarle el input. Generar una nueva tupla que sea = a la lista y sumarsela a la tupla vacía, finalmente imprimir el resultado.


def crear_lista_tupla(secuencia): 

    for i in secuencia:
   
        if i in secuencia: 
            
            lista = []
            lista.append(secuencia)
    
            tupla = ()
            convert = list(tupla)
            convert.append(secuencia)
            convertir = tuple(convert)
            tupla += convertir
    
            print("Lista: ", lista)
            print("Tupla: ", tupla) 
            break

secuencia = (input("Ingrese una secuencia de números separados por comas: ")) 
crear_lista_tupla(secuencia)

       
  