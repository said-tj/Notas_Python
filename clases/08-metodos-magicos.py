class Perro:
    # El contructor es un método mágico
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __del__(self):
        print(f"Caho perro {self.nombre}")

    def __str__(self):
        return f"Clase Perro: {self.nombre}"

    def habla(self):
        print(f"{self.nombre} dice: Guau!")


# Todos los métodos mágicos siempre van a comenzar con __ y van a terminar con__.
perro = Perro("Palomo", 10)
del perro
