
seguirChateando = True
while seguirChateando:
    texto = input(">")
    if texto == "salir":
        seguirChateando = False
    texto = texto.replace( ":)", " 😊 ")
    texto = texto.replace( ":*", " 😘 ")
    texto = texto.replace( ":p", " 😏 ")
    print(texto)
    
 
