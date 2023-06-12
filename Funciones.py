def saludar(nombre):
    print(f"Hola Bienvenido {nombre}")



saludar("Jose")

#Eliminar un registro

lista = [10,50,100,500,1000,5000]

def eliminar(valor):
    lista.remove(valor)

#num = int(input("Ingrese un valor"))

#eliminar(num)

print(lista)

#Sumar todos los valores de lista 
def calcularLista():
    total = 0 
    for i in lista:
        total+=i
    return total

sumaLista = calcularLista()

print(f"La suma de todos los valores de la lista es: {calcularLista()}")