# Santiago José Gutiérrez Guillén
# Ejercicio 10
# Enunciado: Escribir dos funciones que permitan calcular:
# La cantidad de segundos en un tiempo dado en horas, minutos y segundos.
# La cantidad de horas, minutos y segundos de un tiempo dado en segundos.
# Escribe un programa principal con un menú donde se pueda elegir la opción de convertir a segundos, convertir a horas,minutos y segundos o salir del programa.

from Funciones10 import segundos_a_horas_minutos_segundos
from Funciones10 import horas_minutos_segundos_a_segundos

def main():
    while True:
        print("Menú:")
        print("1. Convertir a segundos")
        print("2. Convertir a horas, minutos y segundos")
        print("3. Salir")

        opcion_gutierrez = int(input("Ingrese la opción deseada: "))

        if opcion_gutierrez == 1:
            horas_gutierrez = int(input("Ingrese las horas: "))
            minutos_gutierrez = int(input("Ingrese los minutos: "))
            segundos_gutierrez = int(input("Ingrese los segundos: "))
            total_segundos_gutierrez = horas_minutos_segundos_a_segundos(horas_gutierrez, minutos_gutierrez, segundos_gutierrez)
            print("La cantidad de segundos es: ", total_segundos_gutierrez)
        elif opcion_gutierrez == 2:
            segundos_gutierrez = int(input("Ingrese los segundos: "))
            horas_gutierrez, minutos_gutierrez, segundos_gutierrez = segundos_a_horas_minutos_segundos(segundos_gutierrez)
            print("La cantidad de horas, minutos y segundos es: ", horas_gutierrez, ":", minutos_gutierrez, ":", segundos_gutierrez)
        elif opcion_gutierrez == 3:
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    main()