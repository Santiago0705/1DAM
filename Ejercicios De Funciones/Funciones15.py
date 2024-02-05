# Funciones Del Ejercicio 15: es lo mismo que el ejercicio anterior pero sustituyendo la palabra pila por cola.

def LongitudCola(cola_gutierrez):
    return len(cola_gutierrez)

def EstaVaciaCola(cola_gutierrez):
    return len(cola_gutierrez) == 0

def EstaLlenaCola(cola_gutierrez, capacidad_gutierrez):
    return len(cola_gutierrez) == capacidad_gutierrez

def AddCola(elemento_gutierrez, cola_gutierrez, capacidad_gutierrez):
    if not EstaLlenaCola(cola_gutierrez, capacidad_gutierrez):
        cola_gutierrez.append(elemento_gutierrez)
        print(f"Elemento '{elemento_gutierrez}' añadido a la cola.")
    else:
        print("Error: La cola está llena. No se puede añadir más elementos.")

def SacarDeLaCola(cola_gutierrez):
    if not EstaVaciaCola(cola_gutierrez):
        elemento_gutierrez = cola_gutierrez.pop(0)
        print(f"Elemento '{elemento_gutierrez}' sacado de la cola.")
        return elemento_gutierrez
    else:
        print("Error: La cola está vacía. No se puede sacar ningún elemento.")
        return None

def EscribirCola(cola_gutierrez):
    print("Contenido de la cola:")
    for elemento_gutierrez in cola_gutierrez:
        print(elemento_gutierrez)
