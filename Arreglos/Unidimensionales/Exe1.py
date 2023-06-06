import numpy as np
import random

#np.random.randint(inicio,fin,(dimension/shape))
#Permite generar un array con valores random de una dimension en especifico
arreglo = np.random.randint(0,500,(100))

print(arreglo)
#Mostrar solo indices pares
for i in range(arreglo.size):
    if i%2==0:
        print(arreglo[i])
print("---------------------------")
#Mayor
print(f"El dato de mayor valor del arreglo es {arreglo.max()}")
#Indice posicion mayor dato
for i in range(arreglo.size):
    if arreglo[i]==arreglo.max():
        print(f"La posicion del mayor dato del arreglo es {i}")
        
#Menor
print(f"El valor de menor valor del arreglo es: {arreglo.min()}")

#Copia y multi x 3
arregloB = arreglo
arregloB*=3
#print(arreglo)
print(arregloB)

#Suma del segundo arreglo
print(arregloB.sum())

#Promedio segundo arreglo
print(arregloB.mean())