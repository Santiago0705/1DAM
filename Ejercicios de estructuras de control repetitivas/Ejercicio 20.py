# Santiago José Gutierrez Guillén
# Ejercicio 20
# Mostrar en pantalla los N primero número primos. Se pide por teclado la cantidad de números primos que queremos mostrar.

n_gutierrez = input("Ingrese la cantidad de números primos que desea mostrar: ")

if not n_gutierrez.isdigit():
    print("Por favor, ingrese un número entero válido.")
    exit()

n_gutierrez = int(n_gutierrez)

if n_gutierrez <= 0:
    print("Por favor, ingrese un número positivo mayor que cero.")
    exit()

numeros_primos_gutierrez = []
i_gutierrez = 2

while len(numeros_primos_gutierrez) < n_gutierrez:
    es_primo_gutierrez = True
    for j_gutierrez in range(2, int(i_gutierrez**0.5) + 1):
        if i_gutierrez % j_gutierrez == 0:
            es_primo_gutierrez = False
            break

    if es_primo_gutierrez:
        numeros_primos_gutierrez.append(i_gutierrez)
    i_gutierrez += 1

print(f"Los primeros {n_gutierrez} números primos son: {numeros_primos_gutierrez}")
