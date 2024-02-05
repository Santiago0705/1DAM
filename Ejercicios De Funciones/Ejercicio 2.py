# Santiago José Gutiérrez Guillén
# Ejercicio 2
# Enunciado: Crea un programa que pida dos número enteros al usuario y diga si alguno de ellos es múltiplo del otro. Crea una función EsMultiplo que reciba los dos números, 
# y devuelve si el primero es múltiplo del segundo.

from Funciones2 import es_multiplo

# Pide dos números al usuario
num1_gutierrez = int(input("Introduce el primer número: "))
num2_gutierrez = int(input("Introduce el segundo número: "))

# Comprueba si alguno de los dos números es múltiplo del otro
if es_multiplo(num1_gutierrez, num2_gutierrez):
    print(f"{num1_gutierrez} es múltiplo de {num2_gutierrez}")
elif es_multiplo(num2_gutierrez, num1_gutierrez):
    print(f"{num2_gutierrez} es múltiplo de {num1_gutierrez}")
else:
    print("Ninguno de los dos números es múltiplo del otro")