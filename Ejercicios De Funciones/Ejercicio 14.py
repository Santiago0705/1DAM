# Santiago José Gutiérrez Guillén
# Ejercicio 14
# Enunciado: Vamos a crear un programa para trabajar con una pila. Una pila es una estructura de datos que nos permite guardar un conjunto de variables. La característica fundamental es que el último elemento que se añade al conjunto es el primero que se puede sacar.
# Para representar una pila vamos a utilizar una lista de cadenas de caracteres.
# Vamos a crear varias funciones para trabajar con la pila:
# LongitudPila: Función que recibe una pila y devuelve el número de elementos que tiene.
# EstaVaciaPila: Función que recibe una pila y que devuelve si la pila está vacía, no tiene elementos.
# EstaLlenaPila: Función que recibe una pila y que devuelve si la pila está llena.
# AddPila: función que recibe una cadena de caracteres y una pila, y añade la cadena a la pila, si no está llena. si esta llena muestra un mensaje de error.
# SacarDeLaPila: Función que recibe una pila y devuelve el último elemento añadido y lo borra de la pila. Si la pila está vacía muestra un mensaje de error.
# EscribirPila: Función que recibe una pila y muestra en pantalla los elementos de la pila.
# Realiza un programa principal que nos permita usar las funciones anterior, que nos muestre un menú, con las siguientes opciones:
# Añadir elemento a la pila
# Sacar elemento de la pila
# Longitud de la pila
# Mostrar pila
# Salir

from Funciones14 import LongitudPila
from Funciones14 import EstaVaciaPila
from Funciones14 import EstaLlenaPila
from Funciones14 import AddPila
from Funciones14 import SacarDeLaPila
from Funciones14 import EscribirPila

# Programa principal
capacidad_pila_gutierrez = 5
pila_gutierrez = []

while True:
    print("\nMenú:")
    print("1. Añadir elemento a la pila")
    print("2. Sacar elemento de la pila")
    print("3. Longitud de la pila")
    print("4. Mostrar pila")
    print("5. Salir")

    opcion = int(input("Seleccione una opción (1-5): "))

    if opcion == 1:
        elemento_gutierrez = input("Introduce el elemento a añadir a la pila: ")
        AddPila(elemento_gutierrez, pila_gutierrez, capacidad_pila_gutierrez)

    elif opcion == 2:
        SacarDeLaPila(pila_gutierrez)

    elif opcion == 3:
        print(f"Longitud de la pila: {LongitudPila(pila_gutierrez)}")

    elif opcion == 4:
        EscribirPila(pila_gutierrez)

    elif opcion == 5:
        print("¡Hasta luego!")
        break

    else:
        print("Opción no válida. Por favor, seleccione una opción del 1 al 5.")
