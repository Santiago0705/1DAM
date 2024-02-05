# Santiago José Gutiérrez Guillén
# Ejercicio 2
# Escribir una función que pida un número entero entre 1 y 10, lea el fichero primerapellido-n.txt con la tabla de multiplicar de ese número, done n es el número introducido, 
# y la muestre por pantalla. Si el fichero no existe debe mostrar un mensaje por pantalla informando de ello.

def mostrar_tabla_guardada():
    numero_gutierrez = int(input("Introduce un numero entero entre 1 y 10: "))
    nombre_archivo_gutierrez = f"{numero_gutierrez}_gutierrez.txt" 
    
    try:
        with open(nombre_archivo_gutierrez, 'r') as archivo_gutierrez:
            contenido_gutierrez = archivo_gutierrez.read()
            print(f"Tabla de multiplicar del numero {numero_gutierrez}:\n")
            print(contenido_gutierrez)
    except FileNotFoundError:
        print(f"El archivo '{nombre_archivo_gutierrez}' no existe.")

# Llamada a la función
mostrar_tabla_guardada()
