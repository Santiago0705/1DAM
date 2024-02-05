def pedir_nombre():
    nombre = input("Ingrese su nombre: ")
    apellido1 = input("Ingrese su primer apellido: ")
    apellido2 = input("Ingrese su segundo apellido: ")

    # Calcular e imprimir las iniciales
    iniciales = nombre[0] + apellido1[0] + apellido2[0]
    print("Las iniciales del nombre, el primer apellido y el segundo apellido son:", iniciales)

pedir_nombre()