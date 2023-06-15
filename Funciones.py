def saludo():
    print("Bienvenido Usuario")


lista = [10, 50, 100, 500, 1000, 5000]


# sin arg sin return
# Muestre todos los valores de la lista
def listar():
    for i in range(len(lista)):
        print(lista[i])


# sin arg con retorno
def sizeLista():
    return len(lista)


# print(f"El largo de la lista es: {sizeLista()}")
def buscar(valor):
    res = "No se encuentra"
    for x in lista:
        if x == valor:
            res = "Valor existe"
    print(res)


# num = int(input("Ingrese valor a buscar: "))
# buscar(num)


# Eliminar un registro de la lista
def eliminar(valor):
    try:
        lista.remove(valor)
        print("Eliminado con exito")
    except ValueError:
        print("Valor no se encuentra")


#num = int(input("Ingrese un valor"))
#eliminar(num)
#listar()
