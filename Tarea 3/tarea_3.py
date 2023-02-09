from options import elec

op = int(elec)

while op <= 6:

    file = open("logs.txt" , "w")
    file.write("BIENVENIDO A NUESTRO PROGRAMA\n")

    
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
         suma = repr(suma)
         file.write ("El resultado de la suma es: " + suma + "\n")
        
         print(" ")

         op = int(input("Seleccione el número de la operación que desea realizar o 7 para salir: "))
   
         
          
          

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
        resta = repr(resta)
        print("El resultado de la resta es", resta)

        file.write ("El resultado de la resta es: " + resta +"\n" )

        print(" ")
    

        op = int(input("Seleccione el número de la operación que desea realizar o 7 para salir: "))
        
        




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
                multi = repr(multi)
                print(" ")

                print("Resultado: ", multi)
                print("DIGA n PARA TERMINAR, DIGA p PARA CONTINUAR")
                respuesta = input("¿Desea terminar el programa?: ")

                print(" ")
                file.write ("El resultado de la multiplicacion es: " + multi + "\n")
                print("El resultado de la multiplicacion es", multi)

            print(" ")
         
            op = int(input("Seleccione el número de la operación que desea realizar o 7 para salir: "))

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
        div = repr(div)
        print("El resultado de la división es", div)

        file.write ("El resultado de la division es: " + div + "\n")
        print(" ")
         
        op = int(input("Seleccione el número de la operación que desea realizar o 7 para salir: "))





    #FACTORIAL  
     
    if op == 5:
        while True: 
            print("**Factorial**")
            num = int(input("Ingrese un número mayor a 0: ")) 
            factorial = 1
            if num > 0: 
                print("") 
            else: 
                print("Error, el número ingresado debe ser mayor a 0")   
            for i in range(1, num + 1): 
                factorial *= i 
            factorial = repr(factorial)
            if num > 0: 
                print("El factorial de su número es", factorial) 

                file.write ("El resultado de la factorial es: " + factorial + "\n" )
                print("")
            op = int(input("Seleccione el número de la operación que desea realizar o 7 para salir: "))   
            break
                


    #POTENCIA

    if op == 6:
        print("**POTENCIA**")

        print(" ") 
        print("Ingrese el primer número: ")
        a = float(input())
        print("Ingrese el segundo número: ")
        b = float(input()) 
        pot = a**b 
        pot = repr(pot)
        print("El resultado de la potencia es", pot)

        file.write("El resultado de la potencia es: " + pot + "\n")

        print(" ")
         
        op = int(input("Seleccione el número de la operación que desea realizaro 7 para salir: "))

op == 7
print("Gracias por utilizar el programa")
file.write("MUCHAS GRACIAS POR USAR NUESTRO PROGRAMA")
file.close()