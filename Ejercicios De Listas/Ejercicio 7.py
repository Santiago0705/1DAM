# Santiago José Gutiérrez Guillén
# Ejercicio 7
# Programa que declare tres listas ‘lista1’, ‘lista2’ y ‘lista3’ de cinco enteros cada uno, pida valores para 
# ‘lista1’ y ‘lista2’ y calcule lista3=lista1+lista2.

# Crear tres listas con cinco enteros cada una
lista1_gutierrez = []
lista2_gutierrez = []
lista3_gutierrez = []

# Pedir al usuario cinco valores para 'lista1' y 'lista2'
for i_gutierrez in range(5):
    print("Ingrese un valor para 'lista1':")
    valor1_gutierrez = int(input())
    lista1_gutierrez.append(valor1_gutierrez)

    print("Ingrese un valor para 'lista2':")
    valor2_gutierrez = int(input())
    lista2_gutierrez.append(valor2_gutierrez)

# Calcular 'lista3'=lista1+lista2
for i_gutierrez in range(5):
    suma_gutierrez = lista1_gutierrez[i_gutierrez] + lista2_gutierrez[i_gutierrez]
    lista3_gutierrez.append(suma_gutierrez)

# Mostrar 'lista3'
print("La lista 'lista3' resultante es:", lista3_gutierrez)