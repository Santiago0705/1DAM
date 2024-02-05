#  Santiago José Gutiérrez Guillén
# Ejercicio 2
# Enunciado: Realizar un programa que comprueba si una cadena leída por teclado comienza por una subcadena introducida por teclado.

palabra = input("Introduce una palabra: ")
subcadena = input("Introduce una subcadena: ")

if palabra.startswith(subcadena):
    print("La palabra introducida comienza por la subcadena.")
else:
    print("La palabra introducida no comienza por la subcadena.")