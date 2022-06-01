#Definir una función que detecte si una palabra es un palíndromo y devuelva True ó False.

def palindromo(string):
    return list(reversed(string)) == list(string)

# print(palindromo("python")); #Se espera False
# print(palindromo("reconocer")); #Se espera True
# print(palindromo("Neuquén")); #Se espera False

#Challenge: Modificar la función para ignorar espacios, signos de puntuación, y que no haga distinción entre mayúsculas y minúsculas (pueden usar str.lower o str.upper).
# Sugerimos usar el nombre del desafío como un palíndromo de ejemplo:

def palindromo2(string):
    characters=",;.¿?¡! "
    for c in range(len(list(characters))):
        string = (string.replace(characters[c],"")).lower()
    return list(reversed(string)) == list(string)


print(palindromo2("¿Acaso hubo buhos aca?")) #Se espera True