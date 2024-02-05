# Santiago José Gutiérrez Guillén
# Ejercicio 8
# Enunciado: Crear una función recursiva que permita calcular el factorial de un número. Realiza un programa principal donde se lea un entero y se muestre el resultado del factorial.

from Funciones8 import factorial

n_gutierrez = int(input("Ingrese un número entero: "))
resultado_gutierrez = factorial(n_gutierrez)
print("El factorial de", n_gutierrez, "es:", resultado_gutierrez)