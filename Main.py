

from tkinter import E


def encriptar(texto):
    print("El texto a encriptar es: " + texto)

    textoFinal = ""
    for letra in texto:
        textoFinal+= letra + "x"
    return textoFinal


def desencriptar(texto):
    print("El texto a desencriptar es: " + texto)

    textoFinal = ""
    contador = 0
    for letra in texto:
        if contador %2 == 0:
            textoFinal+= letra 
        contador += 1
    return textoFinal


def encriptarArchivo(rutaArchivo):
    archivo = open(rutaArchivo, "r")
    texto = archivo.read()
    archivo.close()
    textoEncriptado = encriptar(texto)

    archivo = open(rutaArchivo, "w")
    archivo.write(textoEncriptado)
    archivo.close()

    print("El texto se encripto correctamente")


def desencriptarArchivo(rutaArchivo):
    archivo = open(rutaArchivo, "r")
    texto = archivo.read()
    archivo.close()
    textoDesencriptado = desencriptar(texto)

    archivo = open(rutaArchivo, "w")
    archivo.write(textoDesencriptado)
    archivo.close()   

    print("El texto se desencripto correctamente")

respuestaEoD = input(" Presione E para encriptar, o D para desencriptar")
rutaArchivo= input("ingrese la ruta del archivo")

if respuestaEoD == "E": 
    encriptarArchivo(rutaArchivo)
else:
   desencriptarArchivo(rutaArchivo)
 

