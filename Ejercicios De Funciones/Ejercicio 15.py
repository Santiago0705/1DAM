# Santiago José Gutiérrez Guillén
# Ejercicio 15
# Enunciado: Vamos a realizar un programa similar al anterior para trabajar con una cola. Una cola es una estructura de datos que nos permite guardar un conjunto de variables. 
# La característica fundamental es que el primer elemento que se añade al conjunto es el primero que se puede sacar.
# En realizada nos sirven todas las funciones del ejercicio anterior menos la función SacarDeLaCola que es la que tienes que modificar.

from Funciones15 import LongitudCola
from Funciones15 import EstaVaciaCola
from Funciones15 import EstaLlenaCola
from Funciones15 import AddCola
from Funciones15 import SacarDeLaCola
from Funciones15 import EscribirCola

# Programa principal
capacidad_cola_gutierrez = 5
cola_gutierrez = []

while True:
    print("\nMenú:")
    print("1. Añadir elemento a la cola")
    print("2. Sacar elemento de la cola")
    print("3. Longitud de la cola")
    print("4. Mostrar cola")
    print("5. Salir")

    opcion = int(input("Seleccione una opción (1-5): "))

    if opcion == 1:
        elemento_gutierrez = input("Introduce el elemento a añadir a la cola: ")
        AddCola(elemento_gutierrez, cola_gutierrez, capacidad_cola_gutierrez)

    elif opcion == 2:
        SacarDeLaCola(cola_gutierrez)

    elif opcion == 3:
        print(f"Longitud de la cola: {LongitudCola(cola_gutierrez)}")

    elif opcion == 4:
        EscribirCola(cola_gutierrez)

    elif opcion == 5:
        print("¡Hasta luego!")
        break

    else:
        print("Opción no válida. Por favor, seleccione una opción del 1 al 5.")

