# Funciones Del Ejercicio 10: trata de crear un menú e introducir un número de segundos por teclado y el program te dice cuantas horas, minutos y segundos son.

def segundos_a_horas_minutos_segundos(segundos_gutierrez):
    horas_gutierrez = segundos_gutierrez // 3600
    minutos_gutierrez = (segundos_gutierrez % 3600) // 60
    segundos_gutierrez = (segundos_gutierrez % 3600) % 60
    return horas_gutierrez, minutos_gutierrez, segundos_gutierrez

def horas_minutos_segundos_a_segundos(horas_gutierrez, minutos_gutierrez, segundos_gutierrez):
    segundos_gutierrez = horas_gutierrez * 3600 + minutos_gutierrez * 60 + segundos_gutierrez
    return segundos_gutierrez