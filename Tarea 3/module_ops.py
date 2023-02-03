
#FACTORIAL 


num = int(input("Hola, coloca un numero:"))

fact = 1

while True:
    for i in range(1, num+1):
        fact = (fact* i)
    if num < 0:
        print("**ERORR EL NUMERO DEBE SER POSITIVO**")
        print(f"Has colocado {num}")
        break
    else:
        print("Tu numero es positivo")
    print(f"y el factorial de {num} es: {fact}")
    break























