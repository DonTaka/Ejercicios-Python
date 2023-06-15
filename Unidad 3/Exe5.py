import funcExe5 as fn

opcion=0

while opcion!=4:
    print("Menu Principal")
    print("1.- Agregar un producto")
    print("2.- Buscar un producto")
    print("3.- Listar productos")
    print("4.- Salir")
    opcion = int(input("Ingrese opcion que desea: "))
    if opcion==1:
        fn.agregar()
    elif opcion==2:
        fn.buscar()
    elif opcion==3:
        fn.listar()
    elif opcion==4:
        print("Gracias por su preferencia \n Powered by Jose Riquelme ")