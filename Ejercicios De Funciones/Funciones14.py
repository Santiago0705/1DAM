# Funciones Del Ejercicio 14: creamos un menu con diferentes temas y vamos seleccionando y comprobando los elementos de la pila.


def LongitudPila(pila_gutierrez):
    return len(pila_gutierrez)

def EstaVaciaPila(pila_gutierrez):
    return len(pila_gutierrez) == 0

def EstaLlenaPila(pila_gutierrez, capacidad_gutierrez):
    return len(pila_gutierrez) == capacidad_gutierrez

def AddPila(elemento_gutierrez, pila_gutierrez, capacidad_gutierrez):
    if not EstaLlenaPila(pila_gutierrez, capacidad_gutierrez):
        pila_gutierrez.append(elemento_gutierrez)
        print(f"Elemento '{elemento_gutierrez}' añadido a la pila.")
    else:
        print("Error: La pila está llena. No se puede añadir más elementos.")

def SacarDeLaPila(pila_gutierrez):
    if not EstaVaciaPila(pila_gutierrez):
        elemento_gutierrez = pila_gutierrez.pop()
        print(f"Elemento '{elemento_gutierrez}' sacado de la pila.")
        return elemento_gutierrez
    else:
        print("Error: La pila está vacía. No se puede sacar ningún elemento.")
        return None

def EscribirPila(pila_gutierrez):
    print("Contenido de la pila:")
    for elemento_gutierrez in reversed(pila_gutierrez):
        print(elemento_gutierrez)
