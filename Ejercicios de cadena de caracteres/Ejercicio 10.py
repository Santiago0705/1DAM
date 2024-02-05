# Santiago José Gutiérrez Guillén
# Ejercicio 10
# Enunciado: Introducir una cadena de caracteres e indicar si es un palíndromo. Una palabra palíndroma es aquella que se lee igual adelante que atrás.

cadena = input("Introduce una cadena de caracteres: ")

if cadena == cadena[::-1]:
    print(f"La cadena {cadena} es un palíndromo.")
else:
    print(f"La cadena {cadena} no es un palíndromo.")
