#Ejercicio Nro 5
#Bidimensional? 2 pisos Vertical = ProductoS Horizontal = datos del producto
#Producto = numeroParte - Nombre - Precio

lista = [['BLK590','Servidor Arris K900',120000]]
print(lista)
MPN = ['ABC123','ASD321','PLR412','DBA555','KLG660','MKL420','DFT120','DLG860','BFA777','ROM560']
def grabar():
    numeroParte = input("Ingrese numero de parte: ")
    existe = False
    for x in MPN:
        numeroParte= numeroParte.upper()
        if numeroParte==x:
            existe =True
            nombre = input("Ingrese nombre del producto: ")
            if len(nombre)>=6:
                precio = int(input("Ingrese precio del producto: "))
                if precio>0:
                    nuevo = [numeroParte,nombre,precio]
                    lista.append(nuevo)
                    print(lista)
                    print("Agregado con exito")
                    break
                else:
                    print("Precio debe ser mayor a 0 ")
            else:
                print("Nombre debe tener minimo 6 caracteres")

    if existe!=True:
        print("Codigo No existe")

def buscar():
    numeroParte = input("Ingrese numero de parte").upper()
    for y in range(len(lista)):
        if numeroParte == lista[y][0]:
            if lista[y][2]>=500:
                #[0] = Numero de Parte
                print(lista[y][0])
                #[1] = Nombre del producto
                print(lista[y][1])
                #[2] = Precio del producto 
                print(lista[y][2])
            else:
                print("No hay stock del producto")

def imprimir():
    print("Catalogo de productos registrados")
    for y in range(len(lista)):
        print(f"Numero de parte: {lista[y][0]}")
        print(f"Nombre del producto: {lista[y][1]}")
        print(f"Precio del producto: ${lista[y][2]}")
        print("------------------------------------")

opcion = 0

while opcion!=4:
    print("Menu principal")
    print("1.- Grabar producto")
    print("2.- Buscar producto")
    print("3.- Ver catalogo de producto")
    print("4.- Salir")
    try:
        opcion = int(input("Ingrese opcion que desea: "))
        if opcion==1:
            grabar()
        elif opcion==2:
            buscar()
        elif opcion==3:
            imprimir()
        elif opcion==4:
            print("Cerrando aplicacion...")
        else:
            print("Opcion no valida")
    except ValueError:
        print("Debe ingresar un numero")