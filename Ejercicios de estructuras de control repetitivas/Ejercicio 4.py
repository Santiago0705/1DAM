# Santiago José Gutiérrez Guillén
# Ejercicio 4
# Realizar un algoritmo que pida números (se pedirá por teclado la cantidad de números a introducir). 
# El programa debe informar de cuantos números introducidos son mayores que 0, menores que 0 e iguales a 0.

# Pedir la cantidad de números a introducir
cantidad_numeros_gutierrez = int(input("Introduce la cantidad de números a introducir: "))

# Inicializar contadores
mayores_cero_gutierrez = 0
menores_cero_gutierrez = 0
iguales_cero_gutierrez = 0

# Bucle para pedir los números y contar
for i_gutierrez in range(cantidad_numeros_gutierrez):
    # Pedir un número al usuario
    num_gutierrez = int(input("Introduce el número" + str(i_gutierrez + 1)+" : "))


    # Comparar y contar
    if num_gutierrez > 0:
        mayores_cero_gutierrez += 1
    elif num_gutierrez < 0:
        menores_cero_gutierrez += 1
    else:
        iguales_cero_gutierrez += 1

# Mostrar resultados
print("Resultados:")
print("Números mayores que 0: ", mayores_cero_gutierrez)
print("Números menores que 0: ", menores_cero_gutierrez)
print("Números iguales a 0: ", iguales_cero_gutierrez)
