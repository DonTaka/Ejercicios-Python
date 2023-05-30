import random 

lista=[]

for i in range(20):
    lista.append(random.randint(1,100))
menor = 0
mayor = 0
#Forma 1 
for i in lista:
    if menor==0:
        menor=i
    elif i<menor:
        menor=i    
    if i>=mayor:
        mayor=i
#Forma 2 hacer un sort ascendente y llamar la posicion 0 y -1 (Sort ordena de menor a mayor osea 0 seria el menor y -1 el ultimo osea el mayor)
lista.sort()
print(lista)
print(f"El numero menor de la lista es {menor}")
print(f"El numero mayor de la lista es {mayor}")
