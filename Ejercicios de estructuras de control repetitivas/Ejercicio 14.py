# Santiago José Gutiérrez Guillén
# Ejercicio 14
# Una persona se encuentra en el kilómetro 70 de una carretera, otra se 
# encuentra en el km 150, los coches tienen sentido opuesto y tienen la 
# misma velocidad. Realizar un programa para determinar en qué kilómetro 
# de esa carretera se encontrarán.

# Kilómetros iniciales de las dos personas
km_persona1_gutierrez = 70
km_persona2_gutierrez = 150

# Velocidad constante de ambas personas
velocidad_gutierrez = float(input("Introduce la velocidad de ambos coches (en km/h): "))

# Calcular el tiempo hasta que se encuentren
tiempo_encuentro_gutierrez = (km_persona2_gutierrez - km_persona1_gutierrez) / velocidad_gutierrez

# Calcular el kilómetro en el que se encontrarán
kilometro_encuentro_gutierrez = km_persona1_gutierrez + velocidad_gutierrez * tiempo_encuentro_gutierrez

# Mostrar el resultado
print(f"\nSe encontrarán en el kilómetro {kilometro_encuentro_gutierrez:.2f} después de {tiempo_encuentro_gutierrez:.2f} horas.")
