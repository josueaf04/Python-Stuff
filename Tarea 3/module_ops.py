from tarea_3 import elec

op = int(elec)


while op <= 6:

    #SUMA
    if op == 1:
         
         print("**SUMA**")

         print(" ")
         print("Ingrese el primer número: ") 
         a = float(input())
         print("Ingrese el segundo número: ")
         b = float(input()) 
         suma = a + b 

         print(" ")

         print("Resultado: ", suma)
    
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

         print("La SUMA TOTAL es: ", suma)
         print(" ")

         op = int(input("Seleccione el número de la operación que desea realizar: "))
   
         
          
          

    #RESTA

    if op == 2:
        op = op + 1
        print("**RESTA**")

        print(" ")
        print("Ingrese el primer número: ") 
        a = float(input())
        print("Ingrese el segundo número: ")
        b = float(input()) 
        resta = a - b 
        print("El resultado de la resta es", resta)

        print(" ")
         
        op = int(input("Seleccione el número de la operación que desea realizar: "))
        
    #MULTIPLICACION
      
    if op == 3:
            op = op + 1
        
            print("**MULTIPLICACION**")

            print(" ")

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

            print(" ")
         
            op = int(input("Seleccione el número de la operación que desea realizar: "))

    # División
    if op == 4:
        op = op + 1 
        print("**División**")

        print(" ")
        print("Ingrese el primer número: ")
        a = float(input())
        print("Ingrese el segundo número: ")
        b = float(input())
        div = a / b 
        print("El resultado de la división es", div)

        print(" ")
         
        op = int(input("Seleccione el número de la operación que desea realizar: "))

    #FACTORIAL  
         
    if op == 5:
        while True:
            print("**FACTORIAL**")

            print(" ")
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
            print(" ")
         
            op = int(input("Seleccione el número de la operación que desea realizar: "))

    #POTENCIA

    if op == 6:
        print("**POTENCIA**")

        print(" ") 
        print("Ingrese el primer número: ")
        a = float(input())
        print("Ingrese el segundo número: ")
        b = float(input()) 
        pot = a**b 
        print("El resultado de la potencia es", pot)

        print(" ")
         
        op = int(input("Seleccione el número de la operación que desea realizar: "))

op == 7
print("Gracias")