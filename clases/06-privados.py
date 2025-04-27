class Perro:
    def __init__(self, nombre, edad):
        self.__nombre = nombre  # __ Esto lo hace una propiedad privada.
        self.edad = edad

    def get_nombre(self):   # Este es un método para acceder a la propiedad privada. Pero no cambiara el valor.
        return self.__nombre

    def set_nombre(self, nombre):   # Este método valida el cambio en el nombre.
        self.__nombre = nombre

    def habla(self):
        print(f"{self.__nombre} dice:Guau!!")


    @classmethod
    def factory(cls):
        return cls("Palomo", 5)

perro1 = Perro.factory()
perro1.habla()
print(perro1.__dict__)  # Muestra un diccionario con los métodos privados.
