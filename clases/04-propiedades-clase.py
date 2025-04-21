class Perro:
    patas = 4
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad    # Propiedad


    def habla(self):
        print(f"{self.nombre} dice: Guau!")


# Instancias.
Perro.patas = 3 # Cambio de propiedades de clase
mi_perro = Perro("Palomo", 1)
mi_perro.patas = 5
mi_perro2 = Perro("Shagui", 1)
print(Perro.patas)
print(mi_perro.patas)
print(mi_perro2.patas)

