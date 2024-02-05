# Santiago José Gutiérrez Guillén
# Ejercicio 8
# Escribe un programa que pida el limite inferior y superior de un intervalo. Si el límite inferior es mayor que
# el superior lo tiene que volver a pedir. A continuación se van introduciendo números hasta que introduzcamos el 0.
# Cuando termine el programa dará las siguientes informaciones:
# La suma de los números que están dentro del intervalo (intervalo abierto).
# Cuantos números están fuera del intervalo.
# He informa si hemos introducido algún número igual a los límites del intervalo.

# Pedir límites del intervalo (asegurarse de que el límite inferior no sea mayor que el superior)
while True:
    limite_inferior_gutierrez = float(input("Introduce el límite inferior del intervalo: "))
    limite_superior_gutierrez = float(input("Introduce el límite superior del intervalo: "))

    if limite_inferior_gutierrez <= limite_superior_gutierrez:
        break
    else:
        print("Error: El límite inferior debe ser menor o igual al límite superior. Inténtalo de nuevo.")

# Inicializar variables
suma_dentro_intervalo_gutierrez = 0
numeros_fuera_intervalo_gutierrez = 0
numeros_iguales_limites_gutierrez = False

# Bucle para introducir números hasta que se introduce 0
while True:
    numero_gutierrez = float(input("Introduce un número (introduce 0 para salir): "))

    if numero_gutierrez == 0:
        break

    # Verificar si el número está dentro, fuera o igual a los límites del intervalo
    if limite_inferior_gutierrez < numero_gutierrez < limite_superior_gutierrez:
        suma_dentro_intervalo_gutierrez += numero_gutierrez
    elif numero_gutierrez == limite_inferior_gutierrez or numero_gutierrez == limite_superior_gutierrez:
        numeros_iguales_limites_gutierrez = True
    else:
        numeros_fuera_intervalo_gutierrez += 1

# Mostrar resultados
print("\nResultados:")
print(f"La suma de los números dentro del intervalo es: {suma_dentro_intervalo_gutierrez}")
print(f"Cantidad de números fuera del intervalo: {numeros_fuera_intervalo_gutierrez}")
if numeros_iguales_limites_gutierrez:
    print("Se introdujo al menos un número igual a los límites del intervalo.")
else:
    print("No se introdujeron números iguales a los límites del intervalo.")
