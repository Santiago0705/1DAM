# Santiago José Gutiérrez Guillén
# Ejercicio 8
# Enunciado: Realizar un programa que lea una cadena por teclado y convierta las mayúsculas a minúsculas y viceversa.

cadena = input("Introduce una cadena de caracteres: ")

cadena_modificada = ""
for char in cadena:
    if char.isupper():
        cadena_modificada += char.lower()
    else:
        cadena_modificada += char.upper()

print(f"La cadena modificada es: {cadena_modificada}")