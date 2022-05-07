# Escribir una función que calcule el promedio de 3 notas y entrege ese valor usando return.
# Reescribir la función anterior modificándola para asignar una importancia al primer examen de 20%, al segundo de 50% y al tercero de 30%.
# Llamar a cada función anterior 3 veces con distintas notas y verificar, mediante la instrucción if, si el alumno aprobó en cada caso (suponga que 4 es la nota de aprobación).


#Función para calcular promedio / n = a la nota
def promedio(n1,n2,n3):
    return (n1+n2+n3)/3


#Función para calcular promedio ponderado / n = a la nota
def ponderado(n1,n2,n3):
    return (n1*0.2+n2*0.5+n3*0.3)

def estaAprobado(p):
    if p >= 4:
        print('Aprobado')
    else:
        print('Desaprobado')

estaAprobado(ponderado(5,7,4))
estaAprobado(ponderado(3,9,7))
estaAprobado(ponderado(5,3,4))
