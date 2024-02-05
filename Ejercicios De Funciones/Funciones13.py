# Funciones Del Ejercicio 13: trata de hacer un menú con diferentes opciones en las que se encuentran: sumar, restar, dividir y multiplicar, y adicionalmente añadimos una opcion para salir.

def Calcular_mcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def Simplificar_fraccion(numerador, denominador):
    mcd = Calcular_mcd(numerador, denominador)
    return numerador // mcd, denominador // mcd

def Leer_fraccion():
    numerador = int(input("Introduce el numerador: "))
    denominador = int(input("Introduce el denominador: "))

    return Simplificar_fraccion(numerador, denominador)

def Escribir_fraccion(fraccion):
    if fraccion[1] == 1:
        print(fraccion[0])
    else:
        print(f"{fraccion[0]}/{fraccion[1]}")

def Sumar_fracciones(fraccion1, fraccion2):
    numerador = fraccion1[0] * fraccion2[1] + fraccion1[1] * fraccion2[0]
    denominador = fraccion1[1] * fraccion2[1]

    return Simplificar_fraccion(numerador, denominador)

def Restar_fracciones(fraccion1, fraccion2):
    numerador = fraccion1[0] * fraccion2[1] - fraccion1[1] * fraccion2[0]
    denominador = fraccion1[1] * fraccion2[1]

    return Simplificar_fraccion(numerador, denominador)

def Multiplicar_fracciones(fraccion1, fraccion2):
    numerador = fraccion1[0] * fraccion2[0]
    denominador = fraccion1[1] * fraccion2[1]

    return Simplificar_fraccion(numerador, denominador)

def Dividir_fracciones(fraccion1, fraccion2):
    numerador = fraccion1[0] * fraccion2[1]
    denominador = fraccion1[1] * fraccion2[0]

    return Simplificar_fraccion(numerador, denominador)
