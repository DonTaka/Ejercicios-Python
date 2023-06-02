import random

# setlist/tupla
lista = []
for i in range(30):
    lista.append(random.randint(1, 100))

print(lista)
lista.sort()
print(lista)
print(f"El numero menor de la lista es: {lista[0]}")
print(f"El numero mayor de la lista es: {lista[-1]}")
