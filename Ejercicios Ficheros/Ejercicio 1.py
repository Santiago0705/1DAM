# Santiago José Gutiérrez Guillén
# Ejercicio 1
# Escribir una función que pida un número entero entre 1 y 10 y guarde en un fichero con el nombre primer apellido-n.txt la tabla de multiplicar de ese número, done n es el número introducido.

def tabla_multiplicar():
    numero_gutierrez = int(input("Introduce un número entero entre 1 y 10: "))
    
    # Verificar que el número está en el rango adecuado
    if numero_gutierrez < 1 or numero_gutierrez > 10:
        print("El número ingresado está fuera del rango válido.")
        return
    
    nombre_archivo_gutierrez = f"{numero_gutierrez}_gutierrez.txt" 
    
    with open(nombre_archivo_gutierrez, 'w') as archivo_gutierrez:
        archivo_gutierrez.write(f"Tabla de multiplicar del {numero_gutierrez}:\n\n")
        for i_gutierrez in range(1, 11):
            resultado_gutierrez = numero_gutierrez * i_gutierrez
            archivo_gutierrez.write(f"{numero_gutierrez} x {i_gutierrez} = {resultado_gutierrez}\n")
    
    print(f"La tabla de multiplicar del número {numero_gutierrez} se ha guardado en el archivo '{nombre_archivo_gutierrez}'.")

# Llamada a la función
tabla_multiplicar()