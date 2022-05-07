# Escriba un programa que reciba un numero del usuario y repita el siguiente proceso usando un while:
# Si el número es par, se debe dividir por 2 .
# Si el número es impar, se debe multiplicar por 3 y sumar  1 .
# Este proceso se repite hasta llegar al numero 1 y luego muestra en pantalla la cantidad de pasos que tardó en llegar.

def lothar(number):
    counter = 0
    while number != 1:
        if number % 2 == 0:
            number = number/2
        else:
            number = number*3+1
        counter += 1
    return counter

number = int(input())
print(lothar(number))