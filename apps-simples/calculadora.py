# Datos de entrada.
"""
Solicitar al usuario que ingrese dos números
cualesquiera.
"""
a_numero = float(input("Ingresa el primer número: "))
b_numero = float(input("Ingresa el segundo número: "))


# Procesamiento de datos.
"""
Solicitar al usuario que indique 
que operación se va a realizar.
"""
mensaje_inicial = f"Ingresa que operación quieres hacer con el número {a_numero} y {b_numero}"
mensaje_operaciones = f"suma, resta, multi, div"
print(mensaje_inicial, mensaje_operaciones)

operacion = input("Ingresa la operación: ")

if operacion == "suma":
    r_suma = a_numero + b_numero
    print(r_suma)
elif operacion == "resta":
    r_resta = a_numero - b_numero
    print(r_resta)
elif operacion == "multi":
    r_multi = a_numero * b_numero
    print(r_multi)
elif operacion == "div":
    r_div = a_numero / b_numero
    print(r_div)


def Suma(a,b):
    c = a + b
    print(f"La suma de {a} y {b} es: ", c)

Suma(2,3)

