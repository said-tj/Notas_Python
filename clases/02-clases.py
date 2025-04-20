# Pascal Cases
# Upper Camel Cases

# Los métodos son funciones que se encuentran dentro de una clase
# Absolutamente el parámtro de mi método será self
class Perro:
    def habla(self):
        print("Guau!")

mi_perro = Perro()
mi_perro.habla()
print(isinstance(mi_perro, Perro))