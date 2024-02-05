# Santiago José Gutiérrez Guillén
# Ejercicio 5
# Enunciado:  Si tenemos una cadena con un nombre y apellidos, realizar un programa que muestre las iniciales en mayúsculas.

nombre_completo = input("Introduce tu nombre completo: ")

nombre, apellido1, apellido2 = nombre_completo.split()

print(f"Las iniciales en mayúsculas son: {nombre[0].upper()}{apellido1[0].upper()}{apellido2[0].upper()}")