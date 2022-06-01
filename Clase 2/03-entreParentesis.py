# En este desafío deben programar un linter que verifique la correcta utilización de los paréntesis en un texto.
# La entrada del programa será un texto, que puede contener paréntesis () además de cualquier otra letra o símbolo. 
# Su tarea es determinar que el texto sea válido, lo cual en este caso quiere decir que la utilización de paréntesis es correcta, cada símbolo de apertura se corresponde con uno de cierre. 
# Se debe imprimir True o False en función de si el texto es válido o no.

def esCorrecto(string):
    string = list(string)
    inicio=False
    for c in range(len(string)):
        if string[c] == ')': 
            if inicio == False:
                return print(False)
            else:
                inicio = False
        if string[c] == '(':
            if inicio == True:
                return print(False)
            else:
                inicio = True

    return print(inicio == False)

esCorrecto("Yo (Juan) quiero (necesito) café.") #Se espera True
esCorrecto(" (1*(2+3) ") #Se espera False
esCorrecto(" )(()) " ) #Se espera False
esCorrecto(" ( ) ) ( ( ) ") #Se espera False