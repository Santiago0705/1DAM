# Santiago José Gutiérrez Guillén
# Ejercicio 2
#Crea una aplicación que permita adivinar un número. La aplicación 
#genera un número aleatorio del 1 al 100. A continuación va pidiendo 
#números y va respondiendo si el número a adivinar es mayor o menor 
#que el introducido,a demás de los intentos que te quedan (tienes 10 
#intentos para acertarlo). El programa termina cuando se acierta el 
#número (además te dice en cuantos intentos lo has acertado), si se 
#llega al limite de intentos te muestra el número que había generado.

import random

# Generar un número aleatorio entre 1 y 100
numero_a_adivinar_gutierrez = random.randint(1, 100)

# Inicializar el contador de intentos
intentos_gutierrez = 0
max_intentos_gutierrez = 10

# Bucle para que el usuario adivine el número
while intentos_gutierrez < max_intentos_gutierrez:
    # Pedir un número al usuario
    intento_usuario_gutierrez = int(input("Intenta adivinar el número (entre 1 y 100): "))

    # Incrementar el contador de intentos
    intentos_gutierrez += 1

    # Comparar el número ingresado con el número a adivinar
    if intento_usuario_gutierrez == numero_a_adivinar_gutierrez:
        print(f"¡Felicidades! Lo adivinaste en {intentos_gutierrez} intentos.")
        break
    elif intento_usuario_gutierrez < numero_a_adivinar_gutierrez:
        print("El número a adivinar es mayor. Intentos restantes:", max_intentos_gutierrez - intentos_gutierrez)
    else:
        print("El número a adivinar es menor. Intentos restantes:", max_intentos_gutierrez - intentos_gutierrez)

# Mostrar el número si se agotaron los intentos
if intentos_gutierrez == max_intentos_gutierrez:
    print(f"Lo siento, has agotado tus {max_intentos_gutierrez} intentos. El número era: {numero_a_adivinar_gutierrez}.")
