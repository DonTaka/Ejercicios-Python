#Lista base productos
lista =[['123612JDHRS','Servidor Huawei',220000]]
print(lista)
#Agregar
def agregar():
    try:
        numeroParte = input("Ingrese numero parte: ")
        if len(numeroParte)>=10:
            nombre = input("Ingrese nombre del producto: ")
            if len(nombre)>=6:
                precio = int(input("Ingrese precio del producto: "))
                if precio>0:
                    producto = [numeroParte,nombre,precio]
                    lista.append(producto)
                else:
                    print("Precio debe ser mayor a 0 ")  
            else:
                print("Nombre debe tener minimo 6 caracteres")
        else:
            print("Numero parte debe tener minimo 10 caracteres minimo")
    except ValueError:
        print("error en los valores")

#Buscar   
def buscar():
    numParte = input("Ingrese numero pate que busca ")
    for y in range(len(lista)):
            if lista[y][0]== numParte:
                if lista[y][2]>=500:
                    print(f"Numero de parte: {lista[y][0]}")
                    print(f"Nombre del producto: {lista[y][1]}")
                    print(f"Precio del producto: {lista[y][2]}")
                    break
                else:
                    print("No hay stock del producto")
                    

#Listar
def listar():
    for y in range(len(lista)):
        print(f"Numero de parte: {lista[y][0]}")
        print(f"Nombre del producto: {lista[y][1]}")
        print(f"Precio del producto: {lista[y][2]}")
        print("-----------------------------------")