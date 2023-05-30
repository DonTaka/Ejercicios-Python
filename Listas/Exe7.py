lista = []

for i in range(3):
    palabra = input("Ingrese una palabra: ")
    lista.append(palabra)

cantidad = 0 
for x in lista:
    caracteres = x.__len__()
    if caracteres>=cantidad:
        cantidad=caracteres

for x in lista:
    if x.__len__()==cantidad:
        print(x)

