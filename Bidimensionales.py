import numpy as np

arreglo = np.array([[1,2,3],[4,5,6],[7,8,9]])

#Arreglo unidimensional
arr = np.arange(1,101)
#print(arr)
#Arreglo bidimensional
arr = arr.reshape((10,10))
print(arr)
#Arreglo Multidimensional
#arr = arr.reshape((5,5,4))
#print(arr[0][-1][-1])
#Shape = Me muestra las filas y columnas del arreglo
print(arr.shape)

numero = int(input("Ingrese un numero: "))
for y in range(10):
    for x in range(10):
        if  arr[y][x]==numero:
            print(f"El valor de la coordenada : fila {y} columna {x} es {arr[y][x]}")
