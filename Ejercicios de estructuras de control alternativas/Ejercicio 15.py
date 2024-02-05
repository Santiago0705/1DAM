n = int(input("Ingrese el número de alumnos: "))

if n < 30:
    costo_alumno = 0
    costo_total = 4000
elif n < 40:
    costo_alumno = 95
    costo_total = n * costo_alumno
elif n < 50:
    costo_alumno = 70
    costo_total = n * costo_alumno
elif n < 100:
    costo_alumno = 65
    costo_total = n * costo_alumno
else:
    costo_alumno = 65
    costo_total = n * costo_alumno

print(f"Costo por alumno: {costo_alumno} euros")
print(f"Costo total del viaje: {costo_total} euros")