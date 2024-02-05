# Santiago José Gutiérrez Guillén
# Ejercicio 6
# Enunciado: Diseñar una función que calcule el área y el perímetro de una circunferencia. Utiliza dicha función en un programa principal que lea el radio de una circunferencia y 
# muestre su área y perímetro.

from Funciones6 import calcular_circunferencia

def main():
    radio_gutierrez = float(input("Ingrese el radio de la circunferencia: "))
    resultado_gutierrez = calcular_circunferencia(radio_gutierrez)

    print("Área: ", resultado_gutierrez['area'])
    print("Perímetro: ", resultado_gutierrez['circunferencia'])

if __name__ == "__main__":
    main()