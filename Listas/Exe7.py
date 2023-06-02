lista = []

for i in range(3):
    palabra = input("Ingrese una palabra: ")
    lista.append(palabra)

print(lista)
lista.sort(key=len)
print(f"La palabra con mas letras es {lista[-1]}")
