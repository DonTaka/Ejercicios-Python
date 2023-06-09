import numpy as np
#Unidimensional
arreglo = np.arange(1,101)
print(arreglo)

#Bidimensional
arreglo = arreglo.reshape((10,10))
print(arreglo)
print(arreglo[8,6])
print(arreglo[3,9])
print(arreglo[3,-1])
print(arreglo[9,5])
print(arreglo[-1,5])

#Slice
#Start:Stop:Step
#Primeras 3 filas y los primeros 5 datos
#print(arreglo[0:3,0:5])

#Ultimas 3 filas y datos desde el tercero al septimo
#print(arreglo[-1:-4:-1,2:6])

#Multidimensional
#arreglo = arreglo.reshape((5,5,4))
#print(arreglo)

numero = int(input("Ingrese un numero: "))
for y in range(10):
    for x in range(10):
        if  arreglo[y][x]==numero:
            print(f"El valor de la coordenada : fila {y} columna {x} es {arreglo[y][x]}")
            

arr1 = np.array([[1,2,3],[4,5,6]])
arr2 = np.array([[10,20,30,40],[50,60,70,80]])

#print(np.concatenate((arr1,arr2),axis=0))
print(np.concatenate((arr1,arr2),axis=1))


#Crear un arreglo de dos dimensiones de tamaño 3 x 3
#Con elementos aleatorios de números enteros del 0 al 100.
arreglo = np.arange(1,101)
print(arreglo)
arreglo = arreglo.reshape((10,10))
print(arreglo)

#Rellenar un arreglo bidimensional de 10 x 10 con numeros de 0 a 500
#Randint(Inicio,termino,(filas,columnas))
arr = np.random.randint(0,500,(10,10))
arr.sort()
print(arr)


