#En este ejercicio se analizarán los datos reales de un filtro electrónico pasa-altos (atenúa las frecuencias bajas).
# Los nombres de las columnas son:
# time (s)
# Channel 1 (V)
# Channel 2 (V)
# Identificar y mostrar en pantalla:
# El valor más alto de cada columna
# El valor más bajo de cada columna
# El valor promedio de cada columna

from io import open
from os import path

filePath = path.abspath(path.curdir) + "/Clase 2/csv/mediciones.csv"

file = open(filePath) 

contenido = file.readlines() 

datos = contenido[20:]

time=[]
channel1=[]
channel2=[]

for linea in datos:
    data = linea.split(',')
    time.append(float(data[0]))
    channel1.append(float(data[1]))
    channel2.append(float(data[2].replace("/n","")))

print("El valor más alto de tiempo es de:",max(time),"el más bajo de:",min(time),"y el promedio fue de:",sum(time)/len(datos),".")
print("El valor más alto de channel 1 es de:",max(channel1),"el más bajo de:",min(channel1),"y el promedio fue de:",sum(channel1)/len(datos),".")
print("El valor más alto de channel 2 es de:",max(channel2),"el más bajo de:",min(channel2),"y el promedio fue de:",sum(channel2)/len(datos),".")

# Challenge:
# Los instantes de tiempo en los cual la señal Channel 1 pasa de un valor negativo a un valor positivo
# El intervalo de tiempo entre cada uno de estos sucesos (el periodo de la señal)

#Variables a usar
def derivada(x):
    return [x[i] - x[i-1] for i in range(1,len(x))]

instantes = []
signo = 0

for i in range(1, len(channel1)):
  if channel1[i] > 0:
    if signo == -1:
      instantes.append(time[i])
    signo = 1
  elif channel1[i] < 0:
    signo = -1
    
print( instantes )
print( derivada(instantes) )