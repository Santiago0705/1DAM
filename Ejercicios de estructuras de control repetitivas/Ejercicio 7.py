# Santiago José Gutiérrez Guillén
# Ejercicio 7
# Realizar una algoritmo que muestre la tabla de multiplicar de un
# número introducido por teclado.

numero_gutierrez = int(input("Introduce un número para obtener su tabla de multiplicar: "))

print("Tabla de multiplicar del", numero_gutierrez, ":")

for i_gutierrez in range(1, 11):
    resultado_gutierrez = numero_gutierrez * i_gutierrez
    print(numero_gutierrez, "x", i_gutierrez, "=", resultado_gutierrez)