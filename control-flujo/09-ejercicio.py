mensaje = """
Bienvenidos a la calculadora
Para salir escribe Salir
Las operaciones son suma, multi, div y resta
"""
print(mensaje)
n1 = int(input("Ingresa número: "))
operacion = input("Ingresa operación: ")

while operacion != "Salir":
    n2 = int(input("Ingresa el siguiente número: "))
    if operacion == "suma":
        n1 += n2
        print(f"El resultdo es {n1}")
    if operacion == "multi":
        n1 *= n2
        print(f"El resultado es {n1}")
    if operacion == "div":
        n1 /= n2
        print(f"El resultado es {n1}")
    if operacion == "resta":
        n1 -= n2
        print(f"El resultado es {n1}")
    operacion = input("Ingresa operación: ")
