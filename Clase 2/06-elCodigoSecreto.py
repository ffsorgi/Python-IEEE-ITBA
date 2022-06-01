# La idea de este ejercicio es programar lo que sería el agente emisor del mensaje. 
# Para ello, el programa deberá elegir de forma aleatoria un número de 5 cifras y, cada vez que el usuario le ingrese un número por consola, deberá indicar la cantidad de correctos y mal ubicados. 
# El programa termina cuando el usuario adivina el número.

import random

def preguntar():
    return list(input("Inserte el número:"))

emisor = list(str(random.randint(10000, 99999)))

usuario = preguntar()

while emisor != usuario:
    malubicados = 0
    malubicados_list = []
    acertados = 0
    for i in range(5):
        if usuario[i] == emisor[i]:
            acertados +=1
        else:
            if usuario[i] is not malubicados_list:
                malubicados_list.append(usuario[i])
                for n in range (i,5):
                    if usuario[i] == emisor[n]:
                        malubicados += 1
    print("La cantidad de acertados fue de:",acertados,"y la cantidad de mal ubicados fue de:",malubicados)
    usuario = preguntar()