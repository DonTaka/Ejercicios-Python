lista = []

numero = 1

while numero != 0:
    numero = int(input("Ingrese un numero"))
    if numero > 0:
        lista.append(numero)

lista.sort()
print(lista)
