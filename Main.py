# calculadora indice de masa corporal
#IMC = peso / (altura x altura)
 # < 19: delgadez
 # entre 20 y 25: normal
 # entre 26 y 30: sobrepeso
 # > de 30: obesidad

def calcularIMC(peso, alturaM):
    imc = peso / (alturaM * alturaM)
    return imc


def pedirElIMC():
    peso = int(input("Ingrese su peso en kg: "))
    alturaCm = int(input("Ingrese su altura en cm: "))
    alturaM  = alturaCm / 100

    imc = calcularIMC( peso, alturaM)
    print("su indice de masa corporal es de : "+ str(imc))

    if imc < 20:
        print("Estado de delgadez")
    if imc >= 20 and imc < 26:
        print("peso normal")
    if imc >= 26 and imc < 30:
        print("Estado de sobrepeso")
    if imc >= 30:
        print("Estado de obesidad")

print("Calcular el IMC de la primer persona ")
pedirElIMC()
print("Calcular el IMC de la segunda persona ")
pedirElIMC()
print("Calcular el IMC de la tercer persona ")
pedirElIMC()