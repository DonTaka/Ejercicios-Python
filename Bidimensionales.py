import numpy as np

arreglo2 = np.arange(1,101).reshape((10,10))
lista = [[1,2,3],[4,5,6],[7,8,9]]

arreglo = np.array(lista)
print(arreglo2)
#print(arreglo[2][2])
#Recorrido con doble for Y para eje vertical X para eje horizontal
#Guiarse principalmente con la figura 
for y in range(3):
    for x in range(3):
        print(arreglo[y][x])
        
print(arreglo[1::][:2:])