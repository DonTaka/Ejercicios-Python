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

c = [i for i in range(1, 11)]
c = np.array(c)
print(c)

# Recorrido obteniendo largo con LEN
for x in range(len(c)):
    print(c[x])
# Recorrido general usando arreglo como largo
for x in c:
    print(x)

# arange = Rellena arreglo con datos segun indicacion
# (Donde empiezo , donde termino - 1 , de cuanto en cuanto cuento)
arreglo2 = np.arange(1, 11)
print(arreglo2)
