# Santiago José Gutiérrez Guillén
# Ejercicio 7
# Enunciado: Crear una subrutina llamada “Login”, que recibe un nombre de usuario y una contraseña y te devuelve Verdadero si el nombre de usuario es “usuario1” y la contraseña es “asdasd”. 
# Además recibe el número de intentos que se ha intentado hacer login y si no se ha podido hacer login incremente este valor.
# Crear un programa principal donde se pida un nombre de usuario y una contraseña y se intente hacer login, solamente tenemos tres oportunidades para intentarlo.

from Funciones7 import Login

# Programa principal
intentos_gutierrez = 0

while intentos_gutierrez < 3:
    usuario_gutierrez = input("Ingrese su nombre de usuario: ")
    contraseña_gutierrez = input("Ingrese su contraseña: ")
    
    login_correcto_gutierrez = Login(usuario_gutierrez, contraseña_gutierrez, intentos_gutierrez)
    
    if login_correcto_gutierrez:
        print("Inicio de sesión exitoso")
        break
    else:
        print("Nombre de usuario o contraseña incorrecta. Intente nuevamente")
        intentos_gutierrez += 1

if intentos_gutierrez == 3:
    print("Se ha agotado el número máximo de intentos de inicio de sesión")