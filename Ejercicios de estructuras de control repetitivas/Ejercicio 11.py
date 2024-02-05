# Santiago José Gutiérrez Guillén
# Ejercicio 11
# Escribe un programa que diga si un número introducido por teclado es o 
# no primo. Un número primo es aquel que sólo es divisible entre él mismo 
# y la unidad. Nota: Es suficiente probar hasta la raíz cuadrada del número 
# para ver si es divisible por algún otro número.

# Pedir un número al usuario
numero_gutierrez = int(input("Introduce un número para verificar si es primo: "))

# Verificar si el número es primo
if numero_gutierrez < 2:
    es_primo_gutierrez = False
else:
    es_primo_gutierrez = True
    for i_gutierrez in range(2, int(numero_gutierrez**0.5) + 1):
        if numero_gutierrez % i_gutierrez == 0:
            es_primo_gutierrez = False
            break

# Mostrar el resultado
if es_primo_gutierrez:
    print(f"{numero_gutierrez} es un número primo.")
else:
    print(f"{numero_gutierrez} no es un número primo.")
