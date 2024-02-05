# Santiago José Gutiérrez Guillén
# Ejercicio 10
# Algoritmo que muestre la tabla de multiplicar de los números 1,2,3,4 y 5.

# Bucle externo para los números del 1 al 5
for i_gutierrez in range(1, 6):
    print(f"\nTabla de multiplicar del {i_gutierrez}:")
    
    # Bucle interno para multiplicar del 1 al 10
    for j_gutierrez in range(1, 11):
        resultado_gutierrez = i_gutierrez * j_gutierrez
        print(f"{i_gutierrez} x {j_gutierrez} = {resultado_gutierrez}")
