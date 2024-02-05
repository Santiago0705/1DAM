# Funciones Del Ejercicio 8: de lo que trata es de identificar el factorial de un número entero introducido. 

def factorial(n_gutierrez):
    if n_gutierrez == 0 or n_gutierrez == 1:
        return 1
    else:
        return n_gutierrez * factorial(n_gutierrez-1)