import os
import sys


def calcular_sueldo(horas, tarifaN, tarifaE):          # Definimos función para calcular el sueldo
  if horas > 40:
    sueldo = tarifaN * 40 + (horas - 40) * tarifaE
  elif horas <= 40:
    sueldo = tarifaN * horas
  return sueldo


print("Introduzca fichero: ", end="")     # Solicita al usuario el nombre del archivo local a abrir
nombre_fichero = input()

lista_correos = ""                        # Comprueba que el archivo con ese nombre esté en la carpeta de repl.it
contenido_carpeta = os.listdir()
for archivo in contenido_carpeta:
  if archivo == nombre_fichero or archivo[-5::-1] == nombre_fichero[::-1]:
    lista_correos = open(archivo, "r")

if lista_correos == "":
  print("\nNo existe ese directorio.\nFin del programa.")
  sys.exit(0)                             # Si no lo está, el programa termina


for usuario in lista_correos:                                 # Cargamos una lista para cada usuario usando la función split
  datos_usuario = usuario.split(sep=",")

  if str(datos_usuario[0])[-12::] == "@unavarra.es":          # Comprueba el dominio
    salario = calcular_sueldo(int(datos_usuario[1]), int(datos_usuario[2]), int(datos_usuario[3]))  # Llamamos a la función calcular_sueldo
    print("\nEncontrado: " + datos_usuario[0] + "\n" + datos_usuario[1] + " horas, tarifa " + datos_usuario[2] + " y extra " + datos_usuario[3].rstrip('\n') + "\nSueldo: " + str(salario))
  else:                                                       # En caso de dominio externo
    print("\nEncontrado: " + datos_usuario[0] + "\nEl mail no pertenece a nuestra compañía")