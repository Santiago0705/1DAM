# Santiago José Gutiérrez Guillén
# Ejercicio 6
# Escribir un programa que imprima todos los números pares entre dos números que se le pidan al usuario.

numero_inicial_gutierrez = int(input("Introduce el primer número: "))
numero_final_gutierrez = int(input("Introduce el segundo número: "))

print("Los números pares entre", numero_inicial_gutierrez, "y", numero_final_gutierrez, "son:")

for numero_gutierrez in range(numero_inicial_gutierrez, numero_final_gutierrez + 1):
    if numero_gutierrez % 2 == 0:
        print(numero_gutierrez)