# Santiago José Gutiérrez Guillén
# Ejercicio 5
# Escribir un programa que implemente una agenda. En la agenda se podrán guardar nombres y números de teléfono. El programa nos dará el siguiente menú:
# Añadir/modificar: Nos pide un nombre. Si el nombre se encuentra en la agenda, debe mostrar el teléfono y, opcionalmente, permitir modificarlo si no es correcto. Si el nombre no se encuentra, debe permitir ingresar el teléfono correspondiente.
# Buscar: Nos pide una cadena de caracteres, y nos muestras todos los contactos cuyos nombres comiencen por dicha cadena.
# Borrar: Nos pide un nombre y si existe nos preguntará si queremos borrarlo de la agenda.
# Listar: Nos muestra todos los contactos de la agenda.
# Implementar el programa con un diccionario.

agenda_gutierrez = {}

while True:
    print("\nMenú:")
    print("1. Añadir/Modificar contacto")
    print("2. Buscar contacto")
    print("3. Borrar contacto")
    print("4. Listar contactos")
    print("5. Salir")
    
    opcion_gutierrez = input("Ingrese el número de la opcion deseada: ")
    
    if opcion_gutierrez == '1':
        nombre_gutierrez = input("Ingrese el nombre del contacto: ")
        if nombre_gutierrez in agenda_gutierrez:
            print(f"El numero de telefono de {nombre_gutierrez} es: {agenda_gutierrez[nombre_gutierrez]}")
            modificar_gutierrez = input("¿Desea modificar el numero? (sí/no): ")
            if modificar_gutierrez.lower() == 'sí':
                telefono_gutierrez = input("Ingrese el nuevo número de telefono: ")
                agenda_gutierrez[nombre_gutierrez] = telefono_gutierrez
        else:
            telefono_gutierrez = input("Ingrese el numero de telefono: ")
            agenda_gutierrez[nombre_gutierrez] = telefono_gutierrez
            print(f"Contacto {nombre_gutierrez} añadido correctamente.")
    
    elif opcion_gutierrez == '2':
        cadena_gutierrez= input("Ingrese una cadena para buscar contactos: ")
        coincidencias_gutierrez = [nombre_gutierrez for nombre_gutierrez in agenda_gutierrez if nombre_gutierrez.startswith(cadena_gutierrez)]
        if coincidencias_gutierrez:
            print("Contactos encontrados:")
            for contacto_gutierrez in coincidencias_gutierrez:
                print(f"{contacto_gutierrez}: {agenda_gutierrez[contacto_gutierrez]}")
        else:
            print("No se encontraron contactos con esa cadena.")
    
    elif opcion_gutierrez == '3':
        nombre_gutierrez = input("Ingrese el nombre del contacto a borrar: ")
        if nombre_gutierrez in agenda_gutierrez:
            confirmacion_gutierrez = input(f"¿Esta seguro que desea borrar a {nombre_gutierrez} de la agenda? (si/no): ")
            if confirmacion_gutierrez.lower() == 'si':
                del agenda_gutierrez[nombre_gutierrez]
                print(f"Contacto {nombre_gutierrez} borrado de la agenda.")
        else:
            print("El contacto no existe en la agenda.")
    
    elif opcion_gutierrez == '4':
        if agenda_gutierrez:
            print("Lista de contactos en la agenda:")
            for nombre_gutierrez, telefono_gutierrez in agenda_gutierrez.items():
                print(f"{nombre_gutierrez}: {telefono_gutierrez}")
        else:
            print("La agenda esta vacia.")
    
    elif opcion_gutierrez == '5':
        print("¡Hasta luego!")
        break
    
    else:
        print("Opcion no valida. Por favor, ingrese un numero del 1 al 5 para seleccionar una opcion del menu.")
