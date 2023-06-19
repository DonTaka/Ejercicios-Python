import numpy as np

lista= [['BKL512','Servidor Amazon SC1',450]]
MPN =['ASD123','ABC321','QWE436','ZXC312','PLR412','KNG555','OLP333','RPK470','MAP111','USR450']
print(lista)
#Agregar

def agregar():
    codigo = input("Ingrese codigo: ")
    codigo = codigo.upper()
    cod = False
    for i in MPN:
        if codigo == i:
            cod = True
            nombre = input("Ingrese nombre del producto: ")
            if len(nombre)>=6:
                precio = int(input("Ingrese precio: "))
                if precio > 0:
                        nuevo = [codigo,nombre,precio]
                        lista.append(nuevo)
                        print("Producto Agregado con exito")
                        break
                else:
                     print("Precio debe ser mayor a 0 ")
            else:
                 print("Nombre debe tener como minimo 6 caracteres")                 
    if cod!=True:
        print("Codigo no registrado")


agregar()