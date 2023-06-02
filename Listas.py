import random

# Lista inicial

lista = [1, 50, 25, 100, 75]
print("Inicial:   ", lista)

# Append(valor): Agrega un valor en la ultima posicion
lista.append(250)
print("Append:    ", lista)

# Extends([]): Agrega contenido lista2 al final de lista 1
lista2 = [99, 500]
lista.extend(lista2)
print("Extend:    ", lista)

# Insert(posicion,valor): Agrega el valor en la posicion indicada
lista.insert(2, 999)
print("Insert:    ", lista)

# Remove(valor):Entrego un valor , se busca y se elimina
lista.remove(50)
print("Remove:    ", lista)

# Pop():Elimina el ultimo registro de la lista
# Pop(posicion):Elimina el registro de la posicion indicada

lista.pop()
print("Pop:       ", lista)
lista.pop(4)
print("Pop(4):    ", lista)

# Reverse():Invierte el orden de la lista
lista.reverse()
print("Reverse:   ", lista)

# Sort():Ordena de forma ascendente la lista(Menor a Mayor)
lista.sort()
print("Sort:      ", lista)

# Sort(reverse=True):Ordena de forma descendente (Mayor a menor)
lista.sort(reverse=True)
print("Sort(R):   ", lista)


# Randint(inicio,termino): Entrega un numero entre el rango A hasta el B

for i in range(10):
    print(random.randint(1, 1000))

lista = ["aaa", "BBBBBB", "PPPPPPPPPPP"]
lista.reverse()

lista.sort(key=len)
print(lista)
