#Cafeteria
#py -m pip install --upgrade pip
#Actualizar el pip
total = 0 
def calcularBoleta(precio,cantidad):       
    suma = (precio*cantidad)
    print(f" Se agrego ${precio*cantidad} a su boleta")
    return suma

def pagar(total):
    if total>=3000:
        total -=(total*0.1)
        print(f"El total de su compra es ${total} ")
    else:
        print(f"El total de su compra es ${total} ")
#Menu

opcion = 0 

#Espresso - Capuchino - Latte - Moca - Pagar    
while opcion!=5:
    print("Menu de compra ")
    print("1.- Espresso $1.500")
    print("2.- Capuchino $1.800")
    print("3.- Latte $1.600")
    print("4.- Moca $1.700")
    print("5.- Pagar")
    try: 
        opcion = int(input("Que opcion desea: "))
        if opcion==1:
            cantidad = int(input("Cuantos quiere? "))
            total+=calcularBoleta(1500,cantidad)
        elif opcion==2:
            cantidad = int(input("Cuantos quiere? "))
            total+=calcularBoleta(1800,cantidad)
        elif opcion==3:
            cantidad = int(input("Cuantos quiere? "))
            total+=calcularBoleta(1600,cantidad)
        elif opcion==4:            
            cantidad = int(input("Cuantos quiere? "))
            total+=calcularBoleta(1700,cantidad)
        elif opcion==5:
            pagar(total)
        else:
            print("Debe ingresar una opcion entre 1 y 5 ")
    except ValueError:
        print("Debe ingresar un numero")
