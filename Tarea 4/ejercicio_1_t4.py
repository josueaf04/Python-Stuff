# Ejercicio 1 (función que cuenta e imprime en pantalla todos los números, letras y caracteres especiales)

# def contar_caracteres(str): 
#     str="P@#yn26at^&i5ve"    
#     for i in str: 
#         if i.isnumeric(): 
#             num = i
#             return "Números: ", num
#         elif i.isalpha(): 
#             let = i
#             return "Letras: ", let
#         else: 
#             espe = i
#             return "Caracteres especiales", espe
# print(contar_caracteres(str))                     
        

# Ejercicio 2 (función que cuenta todas las apariciones de cada caracter en una string)    

# def contar_apariciones(str): 
str = "papaya"   
    # dict = {} 
for i in str: 
    if i in str: 
        resultado = str.count(i)
        print(resultado)
  