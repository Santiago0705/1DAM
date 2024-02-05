# Santiago José Gutiérrez Guillén
# Ejercicio 3
# Escribir una función que pida dos números n y m entre 1 y 10, lea el fichero primerapellido-n.txt con la tabla de multiplicar de ese número, 
# y muestre por pantalla la línea m del fichero. Si el fichero no existe debe mostrar un mensaje por pantalla informando de ello.

def mostrar_linea_tabla_guardada():
    n_gutierrez = int(input("Introduce un numero entero entre 1 y 10 (n): "))
    m_gutierrez = int(input("Introduce otro numero entero entre 1 y 10 (m): "))
    nombre_archivo_gutierrez = f"{n_gutierrez}_gutierrez.txt" 
    
    try:
        with open(nombre_archivo_gutierrez, 'r') as archivo_gutierrez:
            lineas_gutierrez = archivo_gutierrez.readlines()
            if m_gutierrez <= len(lineas_gutierrez):
                linea_m_gutierrez = lineas_gutierrez[m_gutierrez - 1]  # Restamos 1 para ajustarnos a los índices de Python (comienzan en 0)
                print(f"Linea {m_gutierrez} del archivo '{nombre_archivo_gutierrez}':")
                print(linea_m_gutierrez)
            else:
                print(f"El archivo '{nombre_archivo_gutierrez}' no tiene una linea {m_gutierrez}.")
    except FileNotFoundError:
        print(f"El archivo '{nombre_archivo_gutierrez}' no existe.")

# Llamada a la función
mostrar_linea_tabla_guardada()
