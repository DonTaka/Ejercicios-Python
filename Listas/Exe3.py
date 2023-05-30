lista = []

for i in range(10):
    numero = int(input(f"Ingrese numero {i+1}: "))
    lista.append(numero)
suma=0
promedio=0
for i in lista:
    suma +=i

print(f"La suma de los valores de la lista es {suma}")
print(f"El promedio de valores de la lista es {suma/10}")