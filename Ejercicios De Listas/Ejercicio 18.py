# Santiago José Gutiérrez Guillén
# Ejercicio 18
# Escriba un programa que permita crear una lista de palabras y que, a continuación de tres opciones:
# Contar: Me pide una cadena, y me dice cuantas veces aparece en la lista
# Modificar: Me pide una cadena, y otra cadena a modificar, y modifica todas alas apariciones de la primera por la segunda en la lista.
# Eliminar: Me pide una cadena, y la elimina de la lista.
# Mostrar: Muestra la lista de cadenas
# Terminar

# Crear una lista de palabras
lista_palabras_gutierrez = []

# Ciclo principal del programa
while True:
    print("\nMenú:")
    print("1. Contar")
    print("2. Modificar")
    print("3. Eliminar")
    print("4. Mostrar")
    print("5. Terminar")

    opcion_gutierrez = input("Seleccione una opción: ")

    if opcion_gutierrez == "1":
        palabra_contar_gutierrez = input("Ingrese la palabra a contar: ")
        conteo_gutierrez = lista_palabras_gutierrez.count(palabra_contar_gutierrez)
        print(f"La palabra '{palabra_contar_gutierrez}' aparece {conteo_gutierrez} veces en la lista.")

    elif opcion_gutierrez == "2":
        palabra_modificar_gutierrez = input("Ingrese la palabra a modificar: ")
        palabra_nueva_gutierrez = input("Ingrese la nueva palabra: ")
        lista_palabras_gutierrez = [palabra_nueva_gutierrez if palabra_gutierrez == palabra_modificar_gutierrez else palabra_gutierrez for palabra_gutierrez in lista_palabras_gutierrez]
        print(f"Se modificaron todas las apariciones de '{palabra_modificar_gutierrez}' por '{palabra_nueva_gutierrez}'.")

    elif opcion_gutierrez == "3":
        palabra_eliminar_gutierrez = input("Ingrese la palabra a eliminar: ")
        if palabra_eliminar_gutierrez in lista_palabras_gutierrez:
            lista_palabras_gutierrez = [palabra_nueva_gutierrez for palabra in lista_palabras_gutierrez if palabra != palabra_eliminar_gutierrez]
            print(f"Se eliminó '{palabra_eliminar_gutierrez}' de la lista.")
        else:
            print(f"'{palabra_eliminar_gutierrez}' no está en la lista.")

    elif opcion_gutierrez == "4":
        print("Lista de palabras:", lista_palabras_gutierrez)

    elif opcion_gutierrez == "5":
        print("Saliendo del programa.")
        break

    else:
        print("Opción inválida. Intente de nuevo.")
