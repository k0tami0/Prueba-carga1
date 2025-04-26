class Personaje:

    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.vida = vida

    def atributos(self):
        print(self.nombre, ":", sep="")
        print("Fuerza:", self.fuerza)
        print("Inteligencia:", self.inteligencia)
        print("Defensa:", self.defensa)
        print("Vida:", self.vida)

    def subir_nivel(self,fuerza, inteligencia, defensa):
        self.fuerza = self.fuerza + fuerza
        self.inteligencia = self.inteligencia + inteligencia
        self.defensa = self.defensa + defensa
    
    def esta_vivo(self):
        return self.vida > 0
    
    def esta_muerto(self, vida):
        self.vidavida = 0
        print(f"{self.nombre} ha muerto")

    def daño(self, enemigo):
        return self.fuerza - enemigo.defensa

    def atacar(self, enemigo):
        daño = self.daño(enemigo)
        enemigo.vida = enemigo.vida - daño
    
mi_personaje = Personaje("Osamu", 10, 20, 5, 100)
mi_enemigo= Personaje("Rata", 5, 7, 2, 50)
print(mi_personaje.daño(mi_enemigo))

