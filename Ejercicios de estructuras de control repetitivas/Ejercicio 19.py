# Santiago José Gutierrez Guillén
# Ejercicio 19
# Realizar un ejemplo de menú, donde podemos escoger las distintas opciones hasta que seleccionamos la opción de “Salir”.

while True:
    # Mostrar opciones del menú
    print("Menú:")
    print("1. Opción 1")
    print("2. Opción 2")
    print("3. Opción 3")
    print("4. Salir")

    # Solicitar al usuario que elija una opción
    opcion_gutierrez = input("Seleccione una opción (1-4): ")

    # Verificar la opción seleccionada
    if opcion_gutierrez == "1":
        print("Ha seleccionado la Opción 1.")
        # Agrega aquí el código correspondiente a la Opción 1.

    elif opcion_gutierrez == "2":
        print("Ha seleccionado la Opción 2.")
        # Agrega aquí el código correspondiente a la Opción 2.

    elif opcion_gutierrez == "3":
        print("Ha seleccionado la Opción 3.")
        # Agrega aquí el código correspondiente a la Opción 3.

    elif opcion_gutierrez == "4":
        print("Saliendo del programa. ¡Hasta luego!")
        break  # Sale del bucle while y termina el programa.

    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")
