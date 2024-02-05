# Santiago José Gutiérrez Guillén
# Ejercicio 1
# Enunciado: Codifica un programa en python que solicite información al usuario y nos permita guardar en un diccionario los nombres de tres alumnos de la clase junto con cuatro notas de actividades de clase. 
# A continuación deberá imprimir los tres alumnos con sus notas correspondientes y en el siguiente formato:
# Nombre_de_alumno ha sacado las siguientes notas: ['nota1', 'nota2', 'nota3']

# Solicitar información y guardar en un diccionario
calificaciones_santiago = {}

for i_santiago in range(3):  # Repetir tres veces para ingresar tres alumnos
    nombre_santiago = input("Ingrese el nombre del alumno: ")
    notas_santiago = []
    
    for j_santiago in range(3):  # Repetir tres veces para ingresar las tres notas
        nota_santiago = input(f"Ingrese la nota {j_santiago + 1} de {nombre_santiago}: ")
        notas_santiago.append(nota_santiago)
    calificaciones_santiago[nombre_santiago] = notas_santiago

# Imprimir los alumnos con sus respectivas notas
for alumno_santiago, notas_santiago in calificaciones_santiago.items():
    print(f"{alumno_santiago} ha sacado las siguientes notas: {notas_santiago}")
