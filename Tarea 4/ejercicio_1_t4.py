# Ejercicio 1 (función que cuenta e imprime en pantalla todos los números, letras y caracteres especiales)

# def contar_caracteres(str): 
str="P@#yn26at^&i5ve"
for i in str: 
    if i.isnumeric(): 
        num = i
        print("Números: ", num)
    elif i.isalpha(): 
        let = i
        print("Letras:", let)
    else: 
        espe = i
        print("Caracteres especiales", espe)            
        
    
   