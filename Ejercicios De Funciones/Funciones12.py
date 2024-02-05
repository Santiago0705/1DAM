# Funciones Del Ejercicio 12: mejora el ejercicio 11

from Funciones11 import DiasDelMes

def EsFechaValida(dia_gutierrez, mes_gutierrez, año_gutierrez):
    # Verifica si el año es positivo y el mes y día están en rangos válidos
    return año_gutierrez > 0 and 1 <= mes_gutierrez <= 12 and 1 <= dia_gutierrez <= DiasDelMes(mes_gutierrez, año_gutierrez)

def LeerFecha():
    while True:
        try:
            dia_gutierrez = int(input("Introduce el día (1-31): "))
            mes_gutierrez = int(input("Introduce el mes (1-12): "))
            año_gutierrez = int(input("Introduce el año: "))

            if EsFechaValida(dia_gutierrez, mes_gutierrez, año_gutierrez):
                return dia_gutierrez, mes_gutierrez, año_gutierrez
            else:
                print("Fecha no válida. Por favor, inténtalo de nuevo.")

        except ValueError:
            print("Entrada inválida. Por favor, introduce números enteros.")