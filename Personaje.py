class Personaje: 
    
    #atributos Personaje
    especie = "Humano"
    nombre = "MAster Chief"
    altura = "2.70"
    
    #metodos Personaje
    def correr(self, status):
        if (status):
            print("El personaje " +self.nombre+ " esta corriendo")
        else:
            print("El personaje " +self.nombre+ " se detuvo")
        
    def lanzarGranadas(self):
        print("El personaje " +self.nombre+ " lanzo una granada")
        
    def recargar(self, municiones):
        cargador= 10
        cargador= cargador + municiones
        print ("El arma tiene " + str(cargador) + " balas")