# Ahora les proponemos a ustedes realizar el programa que adivine un número que ustedes elijan, indicándole si los números que este propone son mayores o menores al elegido.
# Ustedes pensarán en un número secreto (para este ejercicio consideremos que el número es menor a 10.000), luego el programa intenta adivinarlo. 
# El usuario debe responder con el símbolo >, < ó =. En el caso de ser igual, el programa termina e imprime la cantidad de intentos que tardó.

maxPosible = 10000
minPosible = 0
respuesta = ''
intentos = 0

print('Escoja un número entre',minPosible,'y',maxPosible,'.')

while respuesta != '=':

    intentos += 1

    #El siguiente número a preguntar
    numero = (maxPosible + minPosible)//2

    print('Su número es >, < o = a',numero,'?')
    respuesta = input()

    #Si es mayor se modifica el mínimo posible al numero consultado + 1
    if respuesta == '>':
        minPosible = numero + 1

    #Si es menor se modifica el máximo posible al numero consultado - 1
    if respuesta == '<':
        maxPosible = numero - 1

print('Encontré el número en:',intentos,'turnos.')