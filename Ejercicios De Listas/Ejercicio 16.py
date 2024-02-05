# Santiago José Gutiérrez Guillén
# Ejercicio 16
# Vamos a crear un programa que tenga el siguiente menú:
# Añadir número a la lista: Me pide un número de la lista y lo añade al final de la lista.
# Añadir número de la lista en una posición: Me pide un número y una posición, y si la posición existe en la lista lo añade a ella (la posición se pide a partir de 1).
# Longitud de la lista: te muestra el número de elementos de la lista.
# Eliminar el último número: Muestra el último número de la lista y lo borra.
# Eliminar un número: Pide una posición, y si la posición existe en la lista lo borra de ella (la posición se pide a partir de 1).
# Contar números: Te pide un número y te dice cuantas apariciones hay en la lista.
# Posiciones de un número: Te pide un número y te dice en que posiciones está (contando desde 1).
# Mostrar números: Muestra los números de la lista
# Salir

lista_gutierrez = []

while True:
    print("Menú:")
    print("1. Añadir número a la lista")
    print("2. Añadir número de la lista en una posición")
    print("3. Longitud de la lista")
    print("4. Eliminar el último número")
    print("5. Eliminar un número")
    print("6. Contar números")
    print("7. Posiciones de un número")
    print("8. Mostrar números")
    print("9. Salir")

    opcion_gutierrez = input("Seleccione una opción: ")

    if opcion_gutierrez == "1":
        num_gutierrez = int(input("Ingrese un número: "))
        lista_gutierrez.append(num_gutierrez)
        print(f"Se añadió {num_gutierrez} a la lista.")

    elif opcion_gutierrez == "2":
        num_gutierrez = int(input("Ingrese un número: "))
        pos_gutierrez = int(input("Ingrese la posición (a partir de 1): "))
        if 1 <= pos_gutierrez <= len(lista_gutierrez) + 1:
            lista_gutierrez.insert(pos_gutierrez - 1, num_gutierrez)
            print(f"Se añadió {num_gutierrez} en la posición {pos_gutierrez}.")

    elif opcion_gutierrez == "3":
        print(f"Longitud de la lista: {len(lista_gutierrez)}")

    elif opcion_gutierrez == "4":
        if lista_gutierrez:
            ultimo_gutierrez = lista_gutierrez.pop()
            print(f"Se eliminó el último número de la lista: {ultimo_gutierrez}")
        else:
            print("La lista está vacía.")

    elif opcion_gutierrez == "5":
        pos_gutierrez = int(input("Ingrese la posición a borrar (a partir de 1): "))
        if 1 <= pos_gutierrez <= len(lista_gutierrez):
            num_borrado_gutierrez = lista_gutierrez.pop(pos_gutierrez - 1)
            print(f"Se eliminó el número {num_borrado_gutierrez} de la posición {pos_gutierrez}.")

    elif opcion_gutierrez == "6":
        num_gutierrez = int(input("Ingrese el número a contar: "))
        conteo_gutierrez = lista_gutierrez.count(num_gutierrez)
        print(f"El número {num_gutierrez} aparece {conteo_gutierrez} veces en la lista.")

    elif opcion_gutierrez == "7":
        num_gutierrez = int(input("Ingrese el número a buscar: "))
        posiciones_gutierrez = [i_gutierrez + 1 for i_gutierrez, x_gutierrez in enumerate(lista_gutierrez) if x_gutierrez == num_gutierrez]
        if posiciones_gutierrez:
            print(f"El número {num_gutierrez} está en las posiciones: {posiciones_gutierrez}")
        else:
            print(f"El número {num_gutierrez} no está en la lista.")

    elif opcion_gutierrez == "8":
        print("Números en la lista:", lista_gutierrez)

    elif opcion_gutierrez == "9":
        print("Saliendo del programa.")
        break

    else:
        print("Opción inválida. Intente de nuevo.")
