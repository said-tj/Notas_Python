n1 = int(input("Ingresa el primer número: "))
n2 = int(input("Ingresa el segundo número: "))

suma = n1 + n2
resta = n1 - n2
produc = n1 * n2
div = n1 / n2

mensaje = f"""
Para los números {n1} y {n2},
el resultdo de la suma es {suma}.
el resultado de la resta es {resta}.
el resultado del producto es {produc}.
el resultado de la división es {div}.
"""

print(mensaje)