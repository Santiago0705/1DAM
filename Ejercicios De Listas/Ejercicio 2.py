# Santiago José Gutiérrez Guillén
# Ejercicio 2
# Crea una lista e inicialízala con 5 cadenas de caracteres leídas por teclado. Copia los elementos 
# de la lista en otra lista pero en orden inverso, y muestra sus elementos por la pantalla.

# Crear e inicializar una lista con 5 cadenas de caracteres leídas por teclado
lista_gutierrez = [input("Ingrese una cadena de caracteres: ") for _ in range(5)]

# Copiar los elementos de la lista en otra lista pero en orden inverso
lista_inversa_gutierrez = lista_gutierrez[::-1]

# Mostrar los elementos de la lista invertida por la pantalla
for cadena_gutierrez in lista_inversa_gutierrez:
    print(cadena_gutierrez)