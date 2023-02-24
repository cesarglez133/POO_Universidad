from Personaje import *

#1. Solicitar datos
print("")
print("###### Datos heroe #######")
especieH = input("Escribe la especie del heroe: ")
nombreH = input("Escribe la nombre del heroe: ")
alturaH = float (input("Escribe la altura del heroe: "))
recargaH =  int (input("Cuantas balas recargas al heroe: "))


print("")
print("###### Datos villano #######")
especieV = input("Escribe la especie del villano: ")
nombreV = input("Escribe el nombre del villano: ")
alturaV =  float (input("Escribe la altura del villano: "))
recargaV = int (input("Cuantas balas recargas al villano: "))

#2. Crear un objeto de la clase personaje
heroe = Personaje(especieH,nombreH,alturaH)
villano = Personaje(especieV,nombreV,alturaV)

#4. Usar atributos
print("")
print("###### Objeto heroe #######")
print("El personaje se llama: " + heroe.getNombre())
print("Pertenece a la especie: " + heroe.getEspecie())
print("Y tiene una altura de: " + str(heroe.getAltura()))

heroe.correr(True)
heroe.lanzarGranadas()
heroe.recargar(recargaH)

print("")
print("###### Objeto villano #######")
print("El personaje se llama: " + villano.getNombre())
print("Pertenece a la especie: " + villano.getEspecie())
print("Y tiene una altura de: " + str(villano.getAltura()))
#5. Usar metodos
villano.correr(False)
villano.lanzarGranadas()
villano.recargar(recargaV)