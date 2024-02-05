# Santiago José Gutiérrez Guillén
# Ejercicio 7
# Enunciado: Pide una cadena y dos caracteres por teclado (valida que sea un carácter), sustituye la aparición del primer carácter en la cadena por el segundo carácter.

cadena = input("Introduce una cadena de caracteres: ")
caracter1 = input("Introduce el primer carácter a reemplazar: ")
caracter2 = input("Introduce el segundo carácter para reemplazar: ")

cadena_modificada = ""
for char in cadena:
    if char == caracter1:
        cadena_modificada += caracter2
    else:
        cadena_modificada += char

print(f"La cadena modificada es: {cadena_modificada}")