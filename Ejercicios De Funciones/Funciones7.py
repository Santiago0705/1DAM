# Funciones Del Ejercicio 7: trata de poner un usuario y contraseña específicos los cuales tienes que introducir.

def Login(usuario_gutierrez, contraseña_gutierrez, intentos_gutierrez):
    if usuario_gutierrez == "usuario1" and contraseña_gutierrez == "asdasd":
        return True
    else:
        intentos_gutierrez += 1
        return False