import random

lista = []

for i in range(20):
    lista.append(random.randint(1, 100))

lista.sort()
print(lista)
