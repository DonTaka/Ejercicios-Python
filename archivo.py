import Funciones as fn

"""
fn.saludo()
fn.listar()

num = int(input("Ingrese un valor: "))
fn.eliminar(num)
"""
opcion = 0
while opcion != 5:
    print("Menu principal")
    print("1.- Saludo")
    print("2.- Mostrar registros de la lista")
    print("3.- Buscar dato en la lista")
    print("4.- Eliminar registro")
    print("5.- Salir")
    opcion = int(input("Ingrese una opcion: "))
    if opcion == 1:
        fn.saludo()
    elif opcion == 2:
        fn.listar()
    elif opcion == 3:
        num = int(input("Ingrese valor  que desea buscar: "))
        fn.buscar(num)
    elif opcion == 4:
        num = int(input("Ingrese valor  que desea buscar: "))
        fn.eliminar(num)
    elif opcion == 5:
        print("Gracias por su preferencia")
    else:
        print("Opcion debe estar en un rango de 1 a 5")
