nombre = input (" como te llamas?")
print("hola " + nombre)

edad = int(input(" cuantos años tienes?"))
masDe12 = edad >= 12
respuestaHijoDelDueño = input(" es hijo del dueño ?")
esHijoDelDueño = respuestaHijoDelDueño == "si"
puedePasar = masDe12 or esHijoDelDueño 

if puedePasar:
    print("Usted puede pasar a la m rusa")
else:
    print("paila")