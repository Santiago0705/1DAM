#  Santiago José Gutiérrez Guillén
# Ejercicio 3
# Enunciado: Pide una cadena y un carácter por teclado (valida que sea un carácter) y muestra cuantas veces aparece el carácter en la cadena.

palabra = input("Introduce una palabra: ")
subcadena = input("Introduce una subcadena: ")

if palabra.startswith(subcadena):
    print("La palabra introducida comienza por la subcadena.")
else:
    print("La palabra introducida no comienza por la subcadena.")

caracter = input("Introduce un carácter: ")
if len(caracter) != 1:
    print("Error: La entrada debe ser un solo carácter.")
else:
    contador = palabra.count(caracter)
    print(f"El carácter '{caracter}' aparece {contador} veces en la palabra.")