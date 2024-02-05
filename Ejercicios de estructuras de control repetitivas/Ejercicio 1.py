# Santiago José Gutiérrez Guillén
# Ejercicio 1
# Crea una aplicación que pida un número y calcule su factorial (El factorial de un número es el producto de todos los
# enteros entre 1 y el propio número y se representa por el número seguido de un signo de exclamación. Por ejemplo 5! = 1x2x3x4x5=120).

# Pedir al usuario que ingrese un número
numero_gutierrez = int(input("Ingrese un número: "))

# Si el número es menor o igual a 1, el factorial es 1
if numero_gutierrez <= 1:
    print("El factorial de", numero_gutierrez, "es 1")

# Si el número es mayor a 1, calcular el factorial
else:
    factorial_gutierrez = 1
    for i_gutierrez in range(1, numero_gutierrez + 1):
        factorial_gutierrez *= i_gutierrez
    print("El factorial de", numero_gutierrez, "es", factorial_gutierrez)