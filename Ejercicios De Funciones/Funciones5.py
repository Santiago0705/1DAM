# Funciones Del Ejercicio 5: lo que hace es analizar diferentes numeros introducidos por teclado e identifica el numero máximo y el numero mínimo.

def calcularmaxmin(lista_gutierrez):
    maximo_gutierrez = max(lista_gutierrez)
    minimo_gutierrez = min(lista_gutierrez)
    return maximo_gutierrez, minimo_gutierrez

# Función para capturar números por teclado
def capturarNumeros():
    lista = []
    while True:
        try:
            num = int(input("Ingrese un número (0 para terminar): "))
            if num == 0:
                break
            lista.append(num)
        except ValueError:
            print("Por favor, ingrese un número válido.")
    return lista