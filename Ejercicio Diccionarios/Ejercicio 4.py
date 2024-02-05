# Santiago José Gutiérrez Guillén
# Ejercicio 4
# Codifica un programa en python que nos permita guardar los nombres de los alumnos de una clase y las notas que han obtenido. Cada alumno puede tener distinta cantidad de notas. 
# Guarda la información en un diccionario cuya claves serán los nombres de los alumnos y los valores serán listas con las notas de cada alumno.
# El programa pedirá el número de alumnos que vamos a introducir, pedirá su nombre e irá pidiendo sus notas hasta que introduzcamos un número negativo. Al final el programa nos 
# mostrará la lista de alumnos y la nota media obtenida por cada uno de ellos. Nota: si se introduce el nombre de un alumno que ya existe el programa nos dará un error.

# Pedir el número de alumnos a introducir
num_alumnos_gutierrez = int(input("Ingrese el número de alumnos: "))

# Diccionario para almacenar nombres y notas de alumnos
alumnos_notas_gutierrez = {}

# Pedir nombres y notas de cada alumno
for i_gutierrez in range(num_alumnos_gutierrez):
    nombre_gutierrez = input(f"Ingrese el nombre del alumno {i_gutierrez + 1}: ")
    notas_gutierrez = []
    while True:
        nota_gutierrez = float(input(f"Ingrese la nota del alumno {nombre_gutierrez} (ingrese un número negativo para terminar): "))
        if nota_gutierrez < 0:
            break
        notas_gutierrez.append(nota_gutierrez)
    
    # Verificar si el nombre ya existe en el diccionario
    if nombre_gutierrez in alumnos_notas_gutierrez:
        print("Error: El nombre del alumno ya existe. Intente con un nombre diferente.")
    else:
        alumnos_notas_gutierrez[nombre_gutierrez] = notas_gutierrez

# Calcular y mostrar la nota media de cada alumno
print("Notas medias de los alumnos:")
for nombre_gutierrez, notas_gutierrez in alumnos_notas_gutierrez.items():
    media_gutierrez = sum(notas_gutierrez) / len(notas_gutierrez)
    print(f"{nombre_gutierrez}: {media_gutierrez:.2f}")
