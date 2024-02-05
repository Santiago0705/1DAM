# Santiago José Gutiérrez Guillén
# Ejercicio 5
# Enunciado: Crea una función “calcularMaxMin” que recibe una lista con valores numéricos y devuelve el valor máximo y el mínimo. Crea un programa que pida números por teclado
# y muestre el máximo y el mínimo, utilizando la función anterior.

from Funciones5 import calcularMaxMin
from Funciones5 import capturarNumeros

# Función principal
def main():
    print("Programa para calcular el máximo y mínimo de una lista de números.")
    numeros_gutierrez = capturarNumeros()
    if numeros_gutierrez:
        maximo_gutierrez, minimo_gutierrez = calcularMaxMin(numeros_gutierrez)
        print(f"El máximo es: {maximo_gutierrez}")
        print(f"El mínimo es: {minimo_gutierrez}")
    else:
        print("No se ingresaron números.")

# Ejecución del programa
if __name__ == "__main__":
    main()