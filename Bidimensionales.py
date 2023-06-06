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


#Ejercicio 1 
#Bidimensional de 3x3 aleatorios de 0 a 100
import random

lista = []

for i in range(9):
    lista.append(random.randint(0,100))

resultado = np.array(lista).reshape((3,3))
print(resultado)