# Función Del Ejercicio 1: se encarga de rercibir el texto mencionado y centrarlo en la panntalla dependiendo de sus caracteres.

def escribir_centrado(texto_gutierrez):
    espacios_gutierrez = 40 - len(texto_gutierrez) // 2
    subrayado_gutierrez = '=' * len(texto_gutierrez)

    print("\n".join([f"{' ' * espacios_gutierrez}{texto_gutierrez}{' ' * espacios_gutierrez}"]))
    print("\n".join([f"{' ' * espacios_gutierrez}{subrayado_gutierrez}{' ' * espacios_gutierrez}"]))