"Elimina repetidos"

list = [1, 2, 3, 3, 2, 4, 6]
eliminar = set(list)
output = [] 
for i in eliminar: 
    output.append(i) 
print(output)