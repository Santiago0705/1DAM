# Funciones Del Ejercicio 9: el programa trata de averiguar el minimo común divisor de dos númeos introducidos por teclado.

def mcd(a_gutierrez, b_gutierrez):
    while(b_gutierrez):
        a_gutierrez, b_gutierrez = b_gutierrez, a_gutierrez % b_gutierrez
    return a_gutierrez