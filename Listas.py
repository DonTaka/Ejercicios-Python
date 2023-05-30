

#Lista inicial
lista = [1,5,25,100,500]
print("Inicial:",lista)
#Append = Agregar un objeto a la ultima posicion
lista.append(999)
print("Append: ",lista)
#insert = Agrega un objeto en una posicion indicada
lista.insert(1,3)
print("Insert: ",lista)
#extend = Agrega los datos de otra lista al final de la lista original
lista.extend([1000,2000])
print("Extend: ",lista)
#Remove = Entrego el dato ,lo busca y lo borra
lista.remove(2000)
print("Remove: ",lista)
#Pop = Borra el ultimo registro de la lista
#Pop(Posicion) = Borra el registro de la posicion indicada
lista.pop()
print("Pop:    ",lista)
lista.pop(5) 
print("Pop(5): ",lista)
#Reverse = Invierte el orden de la lista
lista.reverse()
print("Reverse:",lista)
#Sort = Ordena la lista de menor a mayor
lista.sort()
print("Sort:   ",lista)
#Sort Reverse=True: Ordenado de mayor a menor
lista.sort(reverse=True)
print("Sort(R):",lista)
#Sort con palabras(Extra)
Palabras=["Hola","Adios","Palabra"]
print(Palabras)
Palabras.sort()
print(Palabras)
