import numpy as np

# IMPORTANTE
# Si se quiere usar numpy es necesario instalar la libreria
# PAra hacerlo apretar ctrl + shift + ñ
# escribir pip install numpy
# Esto instalara la libreria que usaremos en la ultima unidad

# Creacion de arreglo con numpy
# np.array() = Generar arreglo con datos de lista en el parentesis
arreglo = np.array([1, 2, 3, 4, 5])
# Start:Stop:Step <----- Estructura general Slice
# Start:: = Indico desde donde debe empezar a usar datos
# :Stop: = Indica hasta donde debe usar datos
# ::Step = Indica de cuanto en cuanto recorre los datos
print(arreglo[::2])

# Ndim = Indica las dimensiones del arreglo
print(arreglo.ndim)

lista = [[[1, 2, 3]]]
arr = np.array(lista)
print(arr)
print("El arreglo es de  ", arr.ndim, " dimensiones")

# len = Permite ver el largo del arreglo
print("El largo del arreglo es : ", len(arreglo))

# Rellenar una lista con ciclo for

arreglo2 = [i for i in range(1, 11)]
arreglo2 = np.array(c)
print(arreglo2)

# Recorrido obteniendo largo con LEN
for x in range(len(arreglo2)):
    print(arreglo2[x])
# Recorrido general usando arreglo como largo
for x in arreglo2:
    print(x)

# arange = Rellena arreglo con datos segun indicacion
# (Donde empiezo , donde termino - 1 , de cuanto en cuanto cuento)
arreglo3 = np.arange(1, 11)
print(arreglo3)

#Sumar valores al arreglo completo
arreglo3+=5
print(arreglo3)

#Multiplicar
arreglo3*=10
print(arreglo3)

#Suma entre arreglos
arreglo3+=arreglo2
print(arreglo3)
#Resta
arreglo3-=arreglo2
print(arreglo3)
#Arr3 es mayor a Arr2
print(arreglo3>arreglo2)
