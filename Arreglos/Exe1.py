import numpy as np

arr = np.arange(1,101).reshape((10,10))
print(arr)
#Mostrar valores 50 - 99 - 15 - 30 
#Mostrar todos los valores de la fila 5
#Mostrar 3 valores de fila 7 usando Slice (misma logica del bidimensional)

#50
print(arr[4][9])
#99
print(arr[-1][-2])
#15
print(arr[1][4])
#30
print(arr[2][-1])


#Parte 2
#[:] = Muestra todos los datos de la columna
print(arr[4][:])

#parte 3 
#Mostrar solo 3 datos de la fila 7

#Slice = Start:Stop:Step 
print(arr[6][0:3])

#Parte 4 
#Mostrar los primeros 4 datos de las primeras 5 filas
print(arr[0:5,0:4])
#Slice con Step
print(arr[0:5:2,0::2])


#Crear un arreglo bidimensional de 3x3 
#Con datos aleatorios de 0 a 100

import random 

lista = []

for i in range(9):
    lista.append(random.randint(0,100))

arreglo = np.array(lista).reshape((3,3))
print(arreglo)
