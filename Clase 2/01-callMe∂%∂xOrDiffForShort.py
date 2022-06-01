# Escribir una función que reciba una lista de precios diarios de las acciones de una compañía. 
# Llamemos n a la cantidad de elementos en esta lista. 
# Debe devolver una lista de tamaño n−1 con los valores de la derivada discreta de la lista recibida.
#Indicar el día en el cual se produjo el mayor salto positivo en el precio de las acciones, y el día en el cual se produjo el mayor salto negativo.

def derivadaDiscreta(precios):
    derivada = []
    n = len(precios)
    for i in range(n-1):
        derivada.insert(i,precios[i+1] - precios[i]) 
    return derivada

precios = [4,4.5,6,20,5.5]

#Nueva lista con los valores de la derivada discreta
vdd= derivadaDiscreta(precios)

print('El día con el mayor salto postitivo fue el día:',vdd.index(max(vdd)),'y el día del mayor salto negativo el:',vdd.index(min(vdd)))