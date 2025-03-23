animal = " Súper Águila "
print(animal.upper())
print(animal.lower())
print(animal.strip().capitalize())
print(animal.title())
print(animal.strip())
print(animal.lstrip()) # Solo quita los espacios de la izquierda.
print(animal.rstrip()) # Solo quita los espacios de la derecha.
print(animal.find("ila"))
print(animal.find("z")) # El -1 indica que no esta en el string.
print(animal.replace("a", "z"))
print("ila" in animal) # Me devuelve el valor boolean, si es que esta lo que busco.
print("ila" not in animal) # Es el equivalente  a lo anterior.
