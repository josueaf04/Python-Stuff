from tarea_3 import elec

op = int(elec)


def suma(a,b):
    return a + b

def resta(a,b):
    return a-b

def division(a,b):
    return a/b

def multiplicacion(a,b):
    return a*b

def potencia(a,b):
    return a**b  



while op <= 6:

    #SUMA
    if op == 1:
        while True:
         print("Ingrese el primer número: ") 
         a = float(input())
         print("Ingrese el segundo número: ")
         b = float(input()) 
         suma = a + b 
         print(" ")

         ("Resultado: ", suma)
    
         print("DIGA n PARA TERMINAR, DIGA p PARA CONTINUAR")
         respuesta = input("Ingrese su respuesta: ")
         while respuesta != "n":
            if respuesta == "p":  
                print("Ingrese otro numero número: ") 
                a = float(input())
                suma = suma + a

                print(" ")

                print("Resultado: ", suma)
                print("DIGA n PARA TERMINAR, DIGA p PARA CONTINUAR")
                respuesta = input("¿Desea terminar el programa?: ")

            print(" ")

            print("El resultado de la suma es", suma)
            break

    #RESTA

    if op == 2:
        print("Ingrese el primer número: ") 
        a = float(input())
        print("Ingrese el segundo número: ")
        b = float(input()) 
        resta = a - b 
        print("El resultado de la resta es", resta)
        
    #MULTIPLICACION
      
    if op == 3:
        while True:
            print("Ingrese el primer número: ") 
            a = float(input())
            print("Ingrese el segundo número: ")
            b = float(input()) 
            multi = a * b 
            print(" ")

            print("Resultado: ", multi)
            
            print("DIGA n PARA TERMINAR, DIGA p PARA CONTINUAR")
            respuesta = input("Ingrese su respuesta: ")
            while respuesta != "n":
                if respuesta == "p":  
                 print("Ingrese otro numero número: ") 
                 a = float(input())
                multi = multi * a

                print(" ")

                print("Resultado: ", multi)
                print("DIGA n PARA TERMINAR, DIGA p PARA CONTINUAR")
                respuesta = input("¿Desea terminar el programa?: ")

                print(" ")

                print("El resultado de la suma es", multi)
                break

    #FACTORIAL  
         
    if op == 5:
        while True:
            a = input("Hola, coloca un numero:")
            b = 1
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

    #POTECIA

    if op == 6: 
        print("Ingrese el primer número: ")
        a = float(input())
        print("Ingrese el segundo número: ")
        b = float(input()) 
        pot = a**b 
        print("El resultado de la potencia es", pot)

op == 7
print('JODASE')