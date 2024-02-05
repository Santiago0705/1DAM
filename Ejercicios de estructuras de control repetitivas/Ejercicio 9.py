# Santiago José Gutiérrez Guillén
# Ejercicio 9
# Escribe un programa que dados dos números, uno real (base) y un entero positivo
# (exponente), saque por pantalla el resultado de la potencia. No se puede utilizar
# el operador de potencia.

# Pedir la base y el exponente al usuario
base_gutierrez = float(input("Introduce la base (número real): "))
exponente_gutierrez = int(input("Introduce el exponente (número entero positivo): "))

# Inicializar el resultado
resultado_gutierrez = 1

# Calcular la potencia sin utilizar el operador de potencia
for _ in range(exponente_gutierrez):
    resultado_gutierrez *= base_gutierrez

# Mostrar el resultado
print(f"{base_gutierrez} elevado a la {exponente_gutierrez} es igual a: {resultado_gutierrez}")
