from Personaje import *

#1. Crear un objeto de la clase personaje
heroe = Personaje()

#2. Usar atributos
print("El personaje se llama: " + heroe.nombre)
print("Pertenece a la especie: " + heroe.especie)
print("Y tiene una altura de: " + heroe.altura)

#3. Usar metodos
heroe.correr(True)
heroe.lanzarGranadas()
heroe.recargar(87)