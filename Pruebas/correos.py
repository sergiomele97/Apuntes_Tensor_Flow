import os
import sys

print("Introduzca fichero:")
nombre_fichero = input()

lista_correos = ""
contenido_carpeta = os.listdir()
for archivo in contenido_carpeta:
  if archivo == nombre_fichero:
    lista_correos = open(archivo, "r")

if lista_correos == "":
  print("No existe ese directorio.\nFin de programa")
  sys.exit(0)