lista = []

for i in range(10):
    numero = int(input("Ingrese un numero: "))
    lista.append(numero)

suma = 0

for x in lista:
    suma += x

print(f"La suma de los valores de la lista es {suma}")
print(f"El promedio de los valores de la lista es {suma/10}")
