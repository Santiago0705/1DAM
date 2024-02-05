# Santiago José Gutiérrez Guillén
# Ejercicio 3
# Enunciado: Crear una función que calcule la temperatura media de un día a partir de la temperatura máxima y mínima. Crear un programa principal, que utilizando la función anterior, vaya 
# pidiendo la temperatura máxima y mínima de cada día y vaya mostrando la media. El programa pedirá el número de días que se van a introducir.

from Funciones3 import calcular_temperatura_media

num_dias_gutierrez = int(input("Introduce el número de días: "))

for i_gutierrez in range(num_dias_gutierrez):
    temp_max_gutierrez = int(input(f"Introduce la temperatura máxima del día {i_gutierrez+1}: "))
    temp_min_gutierrez = int(input(f"Introduce la temperatura mínima del día {i_gutierrez+1}: "))
    
    temp_media_gutierrez = calcular_temperatura_media(temp_max_gutierrez, temp_min_gutierrez)
    print(f"La temperatura media del día {i_gutierrez+1} es: {temp_media_gutierrez} grados")