#Imprimir todos los numeros del 0 al 6
# i = 1
# while i < 6:
 # print(i)
  
# Imprimir todos los numeros del 0 al 6 pero parar si pasa por 3

# i = 1
# while i < 6:
#  print(i) 
 # break
  #i += 1

# i = 0
# while i < 6:
#   i += 1
#   if i == 3: 
#     continue
#   print(i)
  
# i = 1
# while i < 6: 
#     print(i)
#     i += 1
# else: 
#     print("i ya no es menor que 6")

# frutas = ["manzana", "banano", "melon", "piña"]
# for fruta in frutas: 
#     print(fruta)

# frutas = ["manzana", "banana", "melon", "piña"]
# for fruta in frutas: 
#     print(fruta) 
#     if fruta == "banana": 
#         break
    
# for i in range (6): 
#     print("six")

# for i in range(0,6,2): 
#     print("seis 2.0")

frutas = ["manzana", "melon", "piña"]
adjetivos = ["sabrosa", "grande", "suave"]
for fruta in frutas: 
    for adj in adjetivos: 
        print(fruta,adj)
        