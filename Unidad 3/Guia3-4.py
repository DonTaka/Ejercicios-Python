import numpy as np
#1
def exe1():
    arr = np.random.randint(1,100,(10))
    print(arr)
    num = int(input("Ingrese numero: "))
    for x in arr:
        if num ==x:
            print("Numero encontrado")

#2
def exe2():
    y=0
    x=0
    while (y<=3 or y>=6):        
        y = int(input("Ingrese dimension Y: "))
        if(y>=3 and y<=6):
            while(x<=3 or x>=6):
                x = int(input("Ingrese dimension X: "))
                if(x>=3 and x<=6):
                    large = y*x
                    arr =  np.arange(1,large+1).reshape((y,x)) 
                    break
                else:
                    print("X debe estar entre 3 y 6")
            print(arr)
            print(f"La suma de las filas es: {arr[:,:].sum()}")
            break
        else:
            print("Y debe estar entre 3 y 6")

exe2()
