# Santiago José Gutiérrez Guillén
# Ejercicio 5
# Algoritmo que pida caracteres e imprima ‘VOCAL’ si son vocales y ‘NO VOCAL’ en caso contrario, el programa termina cuando se introduce un espacio.

# Establecer la lista de vocales
vocales_gutierrez = ['a', 'e', 'i', 'o', 'u']

# Establecer un bucle infinito
while True:
    # Solicitar un caracter al usuario
    caracter_gutierrez = input("Ingrese un caracter: ")

    # Si el caracter es un espacio, el programa termina
    if caracter_gutierrez == " ":
        break

    # Si el caracter es una vocal, imprimir 'VOCAL'
    if caracter_gutierrez.lower() in vocales_gutierrez:
        print("VOCAL")
    else:
        print("NO VOCAL")