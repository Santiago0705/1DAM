# Santiago José Gutiérrez Guillén
# Ejercicio 8
# Queremos guardar los nombres y la edades de los alumnos de un curso. Realiza un programa que introduzca el nombre y la edad de cada alumno. El proceso de lectura 
# de datos terminará cuando se introduzca como nombre un asterisco (*) Al finalizar se mostrará los siguientes datos:
# Todos lo alumnos mayores de edad.
# Los alumnos mayores (los que tienen más edad)

alumnos_gutierrez = []

while True:
    nombre_gutierrez = input("Introduce el nombre del alumno (* para terminar): ")
    
    if nombre_gutierrez == '*':
        break
    
    edad_gutierrez = int(input("Introduce la edad de {} : ".format(nombre_gutierrez)))
    alumnos_gutierrez.append((nombre_gutierrez, edad_gutierrez))

print("\nAlumnos mayores de edad:")
for nombre_gutierrez, edad_gutierrez in alumnos_gutierrez:
    if edad_gutierrez >= 18:
        print(f"{nombre_gutierrez} - {edad_gutierrez} años")

mayor_edad_gutierrez = max(alumnos_gutierrez, key=lambda x: x[1])[1]
print(f"\nAlumnos mayores:")
for nombre_gutierrez, edad_gutierrez in alumnos_gutierrez:
    if edad_gutierrez == mayor_edad_gutierrez:
        print(f"{nombre_gutierrez} - {edad_gutierrez} años")
