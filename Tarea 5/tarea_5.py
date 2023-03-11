# Función que recibe los parámetros a y b'
# Retorna la suma de estos dos
# a y b se definen como floats y se genera la variable suma, la cual suma los dos valores. 
def sumar(a, b):
        
         a = float(a)
         b = float(b) 
         suma = a + b
         print(f'EL RESULTADO DE LA SUMA ES: {suma}') 
print('TEST SUMAR: \n')         
sumar(100, 200)
sumar(1000, 2000)
sumar(20, 80) 
sumar(5000, 5000)
print("")

# Programación funcional

print('TEST FUNCIONAL: \n')
print(list(map(lambda a, b: a + b, [100], [200])))
print(list(map(lambda a, b: a + b, [1000], [2000])))
print(list(map(lambda a, b: a + b, [20], [80])))
print(list(map(lambda a, b: a + b, [5000], [5000])))
print("")  
print("========================>")
print("")

# Función que recibe el parámetro list
# Retorna el cubo de los números contenidos en list
# Crea una lista vacía 'output', mediante un for se itera sobre list, finalmente se calcula el cubo de cada iteración

def calcular_cubo(list):  
    output = []
    for num in list: 
        num **= 3 
        output.append(num)
    print(output) 
print('TEST CALCULAR CUBO\n')
calcular_cubo([1, 4, 5])
calcular_cubo([6, 7, 8, 9])
calcular_cubo([1, 2])
calcular_cubo([10, 20, 30, 100])
print("")

# Programación funcional "calcular_cubo"
print('TEST FUNCIONAL\n')
print(list(map(lambda x: x ** 3, [1, 4, 5])))
print(list(map(lambda x: x ** 3, [6, 7, 8, 9])))  
print(list(map(lambda x: x ** 3, [1, 2])))
print(list(map(lambda x: x ** 3, [10, 20, 30, 100]))) 
print("")  
print("========================>")
print("")
# Función que recibe como parámetros a y b
# Retorna la resta de los dos parámetros
# Convierte los parámetros en floats y se genera la variable resta, en la cual se da la operación mencionada

def restar(a, b): 
        
        a = float(a)
        b = float(b)
        resta = a - b 
        resta = repr(resta)
        print(F"EL RESULTADO DE LA RESTA ES: {resta}")
print('TEST RESTAR: \n')        
restar(90, 10) 
restar(100, 50)  
restar(400, 250)
restar(9000, 4500)  
print("")   
       
# Programación funcional
print('TEST FUNCIONAL: \n')
print(list(map(lambda a, b: a - b, [90], [10])))
print(list(map(lambda a, b: a - b, [100], [50])))
print(list(map(lambda a, b: a - b, [400], [250])))
print(list(map(lambda a, b: a - b, [9000], [4500])))
print("")  
print("========================>")
print("")


# Función que recibo los parámetros a y b
# Retorna el resultado de la división entre los 2 parámetros
# Transforma los parámetros en floats y finalmente los divide

def dividir(a, b): 
        a = float(a)
        b = float(b)
        div = a / b 
        div = repr(div)
        print(f'EL RESULTADO DE LA DIVISIÓN ES: {div}\n')
print('TEST DIVIDIR: \n')
dividir(90, 2)
dividir(45, 3)
dividir(1000, 2)
dividir(4900, 70)
print("")

# Programación funcional "dividir"

print('TEST FUNCIONAL: \n')        
print(list(map(lambda a, b: a / b , [90], [2])))
print(list(map(lambda a, b: a / b , [45], [3])))
print(list(map(lambda a, b: a / b , [1000], [2])))
print(list(map(lambda a, b: a / b , [4900], [70])))



