lista = []

opcion = 0

while opcion!=2:
    nombre = input("Ingrese un nombre: ")
    opcion = int(input("Desea seguir ingresando?\n 1.- SI \n 2.- NO "))
    lista.append(nombre)
        
cantidad = 0

print(lista)
for x in lista:
    letras = x.__len__()
    if cantidad==0:
        cantidad=letras
    elif letras<=cantidad:
        cantidad=letras

for x in lista:
    letras = x.__len__()
    if letras==cantidad:
        lista.remove(x)

print(lista)

