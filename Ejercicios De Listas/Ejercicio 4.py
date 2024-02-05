# Santiago José Gutiérrez Guillén
# Ejercicio 4
# Programa que declare una lista y la vaya llenando de números hasta que introduzcamos un número negativo. 
# Entonces se debe imprimir el vector (sólo los elementos introducidos).

# Crear e inicializar una lista vacía
lista_gutierrez = []

# Solicitar al usuario que ingrese números hasta que ingrese un número negativo
print("Ingrese números. Para detener el ingreso, ingrese un número negativo.")
while True:
    num_gutierrez = float(input("Ingrese un número: "))
    if num_gutierrez < 0:
        break
    lista_gutierrez.append(num_gutierrez)

# Mostrar los resultados por la pantalla
print("Vector: ", lista_gutierrez)