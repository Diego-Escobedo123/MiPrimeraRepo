import random

nombres = []

def encontrar_nombre(alumno):
    nombre = ""
    for caracter in alumno:
        if caracter == "2":
            break
        nombre += caracter
    return nombre

alumnos = []
with open("./alumnos.txt", "r") as archivo:
    alumnos = archivo.readlines()
    
nombres = [encontrar_nombre(alumno) for alumno in alumnos]
print(nombres)

alumno_escodigo = random.choice(nombres)
print(f"El alumno que tiene que pasar al frente es: { alumno_escodigo }")