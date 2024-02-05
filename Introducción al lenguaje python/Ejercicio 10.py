# Funcion para calcular el promedio de una lista de calificaciones
def calcular_promedio(calificaciones):
    return sum(calificaciones) / len(calificaciones)

# Entrada de datos
calificaciones_parciales = [float(input("Ingrese la calificación del parcial " + str(i+1) + ": ")) for i in range(3)]
calificacion_examen_final = float(input("Ingrese la calificación del examen final: "))
calificacion_trabajo_final = float(input("Ingrese la calificación del trabajo final: "))

# Calculo de la calificación final
calificacion_final = 0.55 * calcular_promedio(calificaciones_parciales) + 0.30 * calificacion_examen_final + 0.15 * calificacion_trabajo_final

# Salida de datos
print("La calificación final en la materia de Algoritmos es: ", calificacion_final)