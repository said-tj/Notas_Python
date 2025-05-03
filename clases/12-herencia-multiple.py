"""
class Animal:
    def comer(self):
        print("comiendo")

    def pasear(self):
        print("paseando animales")


class Perro(Animal):
    def pasear(self):
        print("paseando al perro")


class Palomo(Perro, Animal):    # La herencia multiple, va a tomar de derecha a izquierda.
    def programar(self):
        print("programando")

palomo = Palomo()
palomo.pasear()
"""

class Caminador:
    def caminar(self):
        print("caminando")

class Volador:
    def volar(self):
        print("volando")

class Nadador:
    def nadar(self):
        print("nadando")


class Pato(Volador, Nadador, Caminador):
    def programar(self):
        print("programando")

pato = Pato()
pato.nadar()
pato.caminar()
pato.volar()

