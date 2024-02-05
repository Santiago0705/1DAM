# Santiago José Gutiérrez Guillén
# Ejercicio 2
# Escribe un programa que lea una cadena y devuelva un diccionario con la cantidad de apariciones de cada carácter en la cadena.

# Leer una cadena desde el usuario
cadena_gutierrez = input("Ingrese una cadena: ")

# Crear un diccionario con la cantidad de apariciones de cada carácter
apariciones_gutierrez = {}
for caracter_gutierrez in cadena_gutierrez:
    if caracter_gutierrez in apariciones_gutierrez:
        apariciones_gutierrez[caracter_gutierrez] += 1
    else:
        apariciones_gutierrez[caracter_gutierrez] = 1

# Mostrar el diccionario resultante
print("El diccionario con las apariciones de cada caracter es:")
print(apariciones_gutierrez)
