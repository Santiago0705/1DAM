# Santiago José Gutiérrez Guillén
# Ejercicio 9
# Enunciado: Realizar un programa que compruebe si una cadena contiene una subcadena. Las dos cadenas se introducen por teclado.

cadena = input("Introduce una cadena de caracteres: ")
subcadena = input("Introduce una subcadena: ")

if subcadena in cadena:
    print(f"La subcadena {subcadena} se encuentra en la cadena {cadena}.")
else:
    print(f"La subcadena {subcadena} no se encuentra en la cadena {cadena}.")