# Se pide importar los datos de los últimos 30 días (en total son 30000 datos) y calcular la media, la varianza, la moda y la mediana de la distribución de datos medidos (sin utilizar librerías de estadística). 
# Los datos se encuentran en el archivo ControlCalidadBotellas.csv bajo la columna Fallas.


from io import open
from os import path

filePath = path.abspath(path.curdir) + "/Clase 2/csv/ControlCalidadBotellas.csv"

file = open(filePath)

file.readline()
data = []

for line in file:     
    data.append(int(line.split(',')[1]))

#Se ordena la lista
data.sort()

#Media
media = sum(data)/len(data)

#Varianza
varianza = 0
for y in range(len(data)):
    varianza += (data[y] - media)**2
varianza = varianza/len(data)

#Moda
counter = 0
anterior = min(data)
counter_list=[]
values_list = [min(data)]

for z in range(len(data)):
    if data[z] == anterior:
        counter += 1
    else:
        values_list.append(data[z])
        counter_list.append(counter)
        counter = 1
    anterior = data[z]

moda = values_list[counter_list.index(max(counter_list))]

#Mediana
mediana = data[ len(data) // 2]


print(media) 
print(varianza)
print(moda)
print(mediana)