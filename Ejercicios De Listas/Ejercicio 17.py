# Santiago José Gutiérrez Guillén
# Ejercicio 17
# Crear un programa que añada números a una lista hasta que introducimos un número negativo. A continuación debe crear una nueva 
# lista igual que la anterior pero eliminando los números duplicados. Muestra esta segunda lista para comprobar que hemos eliminados los duplicados.

# Crear la primera lista y agregar números hasta que se introduce un número negativo
numeros_gutierrez = []
while True:
    num_gutierrez = int(input("Ingrese un número (ingrese un número negativo para detenerse): "))
    if num_gutierrez < 0:
        break
    numeros_gutierrez.append(num_gutierrez)

# Crear una nueva lista eliminando los números duplicados
numeros_sin_duplicados_gutierrez = list(set(numeros_gutierrez))

# Mostrar la segunda lista sin duplicados
print("Lista original:", numeros_gutierrez)
print("Lista sin duplicados:", numeros_sin_duplicados_gutierrez)
