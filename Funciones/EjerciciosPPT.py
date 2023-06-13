# CalcularIVA
# IVA = 0.19
def calcularIVA(precio):
    total = precio + (precio * 0.19)
    return total

    # Forma 2
    # precio*=1.19 return precio


precio = int(input("Ingrese precio del producto: "))
print(f"El total con IVA es ${calcularIVA(precio)}")


# CalcularDescuento
def descuento(precio, desc):
    porc = desc / 100
    total = precio - (precio * porc)
    print(f"El precio total del producto con descuento es ${total}")


precio = int(input("Ingrese precio: "))
desc = int(input("Ingrese descuento(1-99)"))
descuento(precio, desc)


# IMC
def IMC(peso, estatura):
    valor = peso / (estatura**2)
    print(f"Su IMC es de {valor}")

    if valor < 18.5:
        print("Esta bajo peso")
    elif valor >= 18.5 and valor <= 24.9:
        print("Adecuado")
    elif valor >= 25 and valor <= 29.9:
        print("Sobrepeso")
    elif valor >= 30 and valor <= 34.9:
        print("Obesidad grado 1")
    elif valor >= 35 and valor <= 39.9:
        print("Obesidad grado 2")
    elif valor >= 40:
        print("Obesidad grado 3")
    return valor


peso = int(input("Ingrese su peso: "))
estatura = float(input("Ingrese su estatura: "))

imc = IMC(peso, estatura)
print("El IMC es ", imc)
