while True:
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

         print("La suma TOTAL es: ", suma)
         break