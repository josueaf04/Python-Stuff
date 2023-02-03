from tarea_3 import elec

rein = elec 

def suma(a,b):
    return a+b

def resta(a,b):
    return a-b

def division(a,b):
    return a/b

def multiplicacion(a,b):
    return a*b

def potencia(a,b):
    return a**b  
while rein <=6:
    print

#SUMA

print("Ingrese el primer número: ") 
a = float(input())
suma_total = sum([i for i in range(1, a + 1)])
print(suma_total)
suma(5)

#RESTA

print("Ingrese el primer número: ") 
a = float(input())
("Ingrese el segundo número: ")
b = float(input()) 
resta = a - b 
print("El resultado de la resta es", resta)
a = input("Hola, coloca un numero:")
b = 1

while True:
 for i in range(1, a+1):
     b = (b* i)
     if a < 0:
        print("**ERORR EL NUMERO DEBE SER POSITIVO**")
        print(f"Has colocado {a}")
        break
    else:
        print(" ")
        print(f"el factorial de {a} es: {b}")
        break





rein ==7
print('JODASE')

















