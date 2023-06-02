lista = []

opcion = "si"

while opcion != "no":
    nombre = input("Ingrese nombre: ")
    lista.append(nombre)

    opcion = input("Desea seguir agregando? \n Si \n No \n").lower()

lista.sort(key=len)
lista.pop(0)
print(lista)
