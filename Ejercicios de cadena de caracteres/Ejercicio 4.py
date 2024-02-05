# Santiago José Gutiérrez Guillén
# Ejercicio 4
# Enunciado: Suponiendo que hemos introducido una cadena por teclado que representa una frase (palabras separadas por espacios), realiza un programa que cuente cuantas palabras tiene.

frase = input("Introduce una frase: ")

palabras = frase.split()
contador_palabras = len(palabras)

print(f"La frase introducida tiene {contador_palabras} palabras.")