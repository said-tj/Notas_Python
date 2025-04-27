class Perro:
    patas = 4

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad    # Propiedad
    #Factory Method
    @classmethod
    def habla(cls): # cls, es una convención para referirse a la clase misma.
        print("Guau!")

    # 
    @classmethod
    def factory(cls):
        return cls("Hi, bro!!", 4)


Perro.habla()
perro1 = Perro("Palomo", 2)
perro2 = Perro("Shagui", 3)
perro3 = Perro.factory()
print(perro3.edad, perro3.nombre)
