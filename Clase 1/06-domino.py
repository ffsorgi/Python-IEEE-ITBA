# Escribir una función que calcule la cantidad de fichas para un juego de dominó completo con fichas que contienen hasta el número n. 
# Nota: ¡No hay fichas repetidas! 2-4 es la misma ficha que 4-2. ¡Observar que en el dominó hay fichas con valor 0!

def cantidadFichas(n):

    #Contador de piezas
    counter = 0

    for x in range(n+1):
        for y in range(x,n+1):
            counter += 1
    
    return counter

#Versión optimizada
def cantidadFichas2(n):
    return ((n+1)*(n+2))//2

#Escribir una función que muestre todas las fichas para un juego de dominó como el anterior, en cualquier orden.

def mostrarFichas(n):
    for a in range(n+1):
        for b in range(a,n+1):
            print(str(a) + '-' + str(b))


# Escribir una función que, dada una cantidad de fichas, calcule cuál es el n (valor máximo) de las fichas. 
# Si el número de fichas no corresponde a la cantidad de fichas de ningún juego de dominó completo retornar -1.

def valorMaximo(number):

    n = 0

    while cantidadFichas2(n) < number:
        n += 1
    
    if cantidadFichas2(n) == number:
        print(n)
    else:
        print(-1)

    

#Llamar a las funciones anteriores con distintos valores para corroborar su funcionamiento
print(cantidadFichas(3)) #Se espera 10
print(cantidadFichas(4)) #Se espera 15
print()
mostrarFichas(3) #Se espera de 0-0 a 3-3
print()
valorMaximo(10) #Se espera 3
valorMaximo(15) #Se espera 4
valorMaximo(5) #Se espera -1