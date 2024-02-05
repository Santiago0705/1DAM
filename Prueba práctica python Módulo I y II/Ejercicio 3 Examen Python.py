# Santiago José Gutiérrez Guillén
# Ejercicio 3
# Enunciado: Escriba un programa en python que permita crear un menú con las siguientes opciones:
# Insertar: Me solicitará una cadena de caracteres que representará los nombres de los alumnos de una clase. Se deberá insertar en la lista al menos 6 nombres y varios repetidos. 
# Contar: Me pide un nombre de alumno y me dice cuantas veces aparece en la lista
# Mostrar: Muestra la lista de alumnos uno debajo de otro
# Terminar
# El programa debe informar de que se ha pulsado una opción correcta.

alumnos_santiago = []  # Lista para almacenar nombres de alumnos

while True:
    print("\nMenú:")
    print("1. Insertar")
    print("2. Contar")
    print("3. Mostrar")
    print("4. Terminar")

    opcion_santiago = input("Seleccione una opción (1-4): ")

    if opcion_santiago == '1':
        # Insertar nombres de alumnos
        for i_santiago in range(6):
            nombre_santiago = input("Ingrese el nombre del alumno: ")
            alumnos_santiago.append(nombre_santiago)
        print("Nombres de alumnos insertados correctamente.")

    elif opcion_santiago == '2':
        # Contar ocurrencias de un nombre
        nombre_buscar_santiago = input("Ingrese el nombre del alumno a buscar: ")
        veces_santiago = alumnos_santiago.count(nombre_buscar_santiago)
        print(f"El nombre '{nombre_buscar_santiago}' aparece {veces_santiago} veces en la lista.")

    elif opcion_santiago == '3':
        # Mostrar la lista de alumnos
        print("\nLista de alumnos:")
        for alumno_santiago in alumnos_santiago:
            print(alumno_santiago)

    elif opcion_santiago == '4':
        # Terminar el programa
        print("¡Hasta luego!")
        break

    else:
        print("Por favor, seleccione una opción válida (1-4).")
