lista = []

for i in range(1, 11):
    lista.append(5 * i)

lista2 = lista.copy()
lista2.sort()

lista3 = lista2.copy()
lista3.sort(reverse=True)

print(lista)
print(lista2)
print(lista3)

