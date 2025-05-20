# Para definir una función
def Hola(nombre = "Said", apellido = "Tecpa"):
    print("Hola!!")
    print(f"Bienvenido {nombre} {apellido} es un gusto.")


def Suma(a, b):
    resultado_suma = a+b
    print(f"El resultado de la suma de {a} y {b} es ", resultado_suma)

def Resta(a, b):
    resultado_resta = a - b
    print(f"El resultado de la resta de {a} y {b} es ", resultado_resta)

def Multiplicacion(a, b):
    resultado_multiplicacion = a * b
    print(f"El resultado de la multiplicación de {a} y {b} es ", resultado_multiplicacion)

def Division(a, b):
    resultado_division = a // b
    print(f"El resultado de la división entera de {a} y {b} es ", resultado_division)


Hola()
print("Soy una calculadora simple de 4 operaciones básicas")
print("1. Suma, 2. Resta, 3. Multiplicación, 4. División entera.")

operacion = int(input("Por favor, ingresa el número de la operación a realizar: "))

if operacion == 1:
    print("Operación Suma.")
    suma_a = float(input("Ingresa el primer número: "))
    suma_b = float(input("Ingresa el segundo número: "))
    Suma(a = suma_a, b = suma_b)
