# Santiago José Gutiérrez Guillén
# Ejercicio 13
# Enunciado: Queremos crear un programa que trabaje con fracciones a/b. Para representar una fracción vamos a utilizar dos enteros: numerador y denominador.
# Vamos a crear las siguientes funciones para trabajar con funciones:
# Leer_fracción: La tarea de esta función es leer por teclado el numerador y el denominador. Cuando leas una fracción debes simplificarla.
# Escribir_fracción: Esta función escribe en pantalla la fracción. Si el dominador es 1, se muestra sólo el numerador.
# Calcular_mcd: Esta función recibe dos número y devuelve el máximo común divisor.
# Simplificar_fracción: Esta función simplifica la fracción, para ello hay que dividir numerador y dominador por el MCD del numerador y denominador.
# Sumar_fracciones: Función que recibe dos funciones n1/d1 y n2/d2, y calcula la suma de las dos fracciones. La suma de dos fracciones es otra fracción cuyo numerador=n1*d2+d1*n2 y denominador=d1*d2. Se debe simplificar la fracción resultado.
# Restar_fracciones: Función que resta dos fracciones: numerador=n1*d2-d1*n2 y denominador=d1*d2. Se debe simplificar la fracción resultado.
# Multiplicar_fracciones: Función que recibe dos fracciones y calcula el producto, para ello numerador=n1*n2 y denominador=d1*d2. Se debe simplificar la fracción resultado.
# Dividir_fracciones: Función que recibe dos fracciones y calcula el cociente, para ello numerador=n1*d2 y denominador=d1*n2. Se debe simplificar la fracción resultado.
# Crear un programa que utilizando las funciones anteriores muestre el siguiente menú:
# Sumar dos fracciones: En esta opción se piden dos fracciones y se muestra el resultado.
# Restar dos fracciones: En esta opción se piden dos fracciones y se muestra la resta.
# Multiplicar dos fracciones: En esta opción se piden dos fracciones y se muestra la producto.
# Dividir dos fracciones: En esta opción se piden dos fracciones y se muestra la cociente.
# Salir

from Funciones13 import Calcular_mcd
from Funciones13 import Simplificar_fraccion
from Funciones13 import Leer_fraccion
from Funciones13 import Escribir_fraccion
from Funciones13 import Sumar_fracciones
from Funciones13 import Restar_fracciones
from Funciones13 import Multiplicar_fracciones
from Funciones13 import Dividir_fracciones

# Programa principal
while True:
    print("\nMenú:")
    print("1. Sumar dos fracciones")
    print("2. Restar dos fracciones")
    print("3. Multiplicar dos fracciones")
    print("4. Dividir dos fracciones")
    print("5. Salir")

    opcion = int(input("Seleccione una opción (1-5): "))

    if opcion == 1:
        fraccion1 = Leer_fraccion()
        fraccion2 = Leer_fraccion()
        resultado = Sumar_fracciones(fraccion1, fraccion2)
        print("Resultado de la suma:")
        Escribir_fraccion(resultado)

    elif opcion == 2:
        fraccion1 = Leer_fraccion()
        fraccion2 = Leer_fraccion()
        resultado = Restar_fracciones(fraccion1, fraccion2)
        print("Resultado de la resta:")
        Escribir_fraccion(resultado)

    elif opcion == 3:
        fraccion1 = Leer_fraccion()
        fraccion2 = Leer_fraccion()
        resultado = Multiplicar_fracciones(fraccion1, fraccion2)
        print("Resultado de la multiplicación:")
        Escribir_fraccion(resultado)

    elif opcion == 4:
        fraccion1 = Leer_fraccion()
        fraccion2 = Leer_fraccion()
        resultado = Dividir_fracciones(fraccion1, fraccion2)
        print("Resultado de la división:")
        Escribir_fraccion(resultado)

    elif opcion == 5:
        print("¡Hasta luego!")
        break

    else:
        print("Opción no válida. Por favor, seleccione una opción del 1 al 5.")
