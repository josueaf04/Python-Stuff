# Ejercicio 1 (función que cuenta e imprime en pantalla todos los números, letras y caracteres especiales)

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
        

# Ejercicio 2 (función que cuenta todas las apariciones de cada caracter en una string)    

# def contar_apariciones(str):  
#     str = "papaya"
#     apa = 0   
#     dict = {} 
#     for i in str: 
        




# Ejercicio 3 (función que elimina todas las apariciones de un elemento en una lista)   
def eliminar_valor(list): 

    list = [20, 30, 40, 20, 5, 100, 5, 20] 
    rep = 0
    for i in list: 
        if i in list: 
            rep += 1
            apa = list.count(i)
        # if i >= 2:
        #     new_list = [list.remove(i)]
    print(apa)          

eliminar_valor(list)   

       
  