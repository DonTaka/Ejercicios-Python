#Calculo IVA


def calculoIVA():
    precio = 50000
    precio *=1.19
    print(f"Precio con IVA: ${precio}")
calculoIVA()
#Calculo Descuento
def descuento(desc):
    precio = 50000
    precio -=precio*(desc/100)
    print(f"Precio con descuento {precio}")
    
des = int(input("Ingrese cuanto descuento desea: "))
descuento(des)
#IMC
def IMC(peso,estatura):
    IMC = peso/(estatura**2)
    print(f"Tiene un IMC de {IMC}")
    if IMC<18.5:
        print("Esta bajo peso")
    elif IMC>18.5 and IMC<=24.9:
        print("Adecuado")
    elif IMC>=25 and IMC<=29.9:
        print("Sobrepeso")
    elif IMC>=30 and IMC<=34.9:
        print("Obesidad grado 1")
    elif IMC>=35 and IMC<=39.9:
        print("Obesidad grado 2")
    elif IMC>=40:
        print("Obesidad grado 3")
        
peso = int(input("Ingrese su peso: "))
estatura = float(input("Ingrese su estatura"))

IMC(peso,estatura)