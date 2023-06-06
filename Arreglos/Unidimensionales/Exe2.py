import numpy as np

arreglo_1 = np.random.randint(0,1000,(10))
#Mostrar todos los datos
print(arreglo_1)

#Contar Pares
#Sumar Impares
pares =0
suma = 0
for i in arreglo_1:
    if i%2==0:
        pares+=1
    else:
        suma+=i

print(f"La cantidad de pares es {pares}")
print(f"La suma de los impares es {suma}")

