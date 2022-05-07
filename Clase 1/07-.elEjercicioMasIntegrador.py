#Se pide calcular una integral definida en un intervalo de una función genérica.
#En lugar de obtener un resultado exacto, realizaremos una aproximación del resultado aplicando la integral de Riemann.

#Integral desde a hasta b con pasos de dx
def integral(f, a, b, dx):
    x = a
    resultado = 0

    while (x+dx) <= b:
        resultado += f(x)*dx
        x += dx

    return resultado

#f(x)
def f(x):
    return 2*x+1

print( integral(f, 0, 1, 0.0001) )