# Santiago José Gutiérrez Guillén
# Ejercicio 6
# Enunciado: Realizar un programa que dada una cadena de caracteres por caracteres, genere otra cadena resultado de invertir la primera.

cadena = input("Introduce una cadena de caracteres: ")

cadena_invertida = ""
for char in cadena:
    cadena_invertida = char + cadena_invertida

print(f"La cadena invertida es: {cadena_invertida}")