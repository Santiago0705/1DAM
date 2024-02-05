# Santiago José Gutiérrez Guillén
# Ejercicio 9
# Enunciado: Crear una función que calcule el MCD de dos número por el método de Euclides. El método de Euclides es el siguiente:
# Se divide el número mayor entre el menor.
# Si la división es exacta, el divisor es el MCD.
# Si la división no es exacta, dividimos el divisor entre el resto obtenido y se continúa de esta forma hasta obtener una división exacta, siendo el último divisor el MCD.
# Crea un programa principal que lea dos números enteros y muestre el MCD.

from Funciones9 import mcd

num1_gutierrez = int(input("Introduce el primer número: "))
num2_gutierrez = int(input("Introduce el segundo número: "))

print("El MCD de", num1_gutierrez, "y", num2_gutierrez, "es:", mcd(num1_gutierrez, num2_gutierrez))