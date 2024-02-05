def calcular_nota_final(respuestas_correctas, respuestas_incorrectas, respuestas_en_blanco):
    # Calcular la nota final
    nota_final = 5 * respuestas_correctas - 1 * respuestas_incorrectas + 0 * respuestas_en_blanco
    
    # Devolver la nota final
    return nota_final

# Solicitar al usuario que ingrese la cantidad de respuestas correctas, incorrectas y en blanco
respuestas_correctas = int(input("Ingrese la cantidad de respuestas correctas: "))
respuestas_incorrectas = int(input("Ingrese la cantidad de respuestas incorrectas: "))
respuestas_en_blanco = int(input("Ingrese la cantidad de respuestas en blanco: "))

# Calcular e imprimir la nota final del estudiante
nota_final = calcular_nota_final(respuestas_correctas, respuestas_incorrectas, respuestas_en_blanco)
print("La nota final del estudiante es:", nota_final)