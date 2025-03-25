def suma(*numeros): #El parámetro se vuelve iterable.
    resultado = 0
    for numero in numeros:
        resultado += numero
    print(resultado)

suma(2, 5, 10)
suma(2, 10)
suma(1, 2, 3, 4, 5)