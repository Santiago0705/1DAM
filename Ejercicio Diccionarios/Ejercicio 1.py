# Santiago José Gutiérrez Guillén
# Ejercicio 1
# Escribe un programa python que pida un número por teclado y que cree un diccionario cuyas claves sean desde el número 1 hasta el número indicado, y los valores sean los cuadrados de las claves.

# Pedir un número por teclado
numero_gutierrez = int(input("Ingrese un numero: "))

# Crear un diccionario con los cuadrados de las claves
diccionario_gutierrez = {i_gutierrez: i_gutierrez**2 for i_gutierrez in range(1, numero_gutierrez+1)}

# Mostrar el diccionario resultante
print("El diccionario creado es:")
print(diccionario_gutierrez)
