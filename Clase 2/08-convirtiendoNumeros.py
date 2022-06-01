# Para poner esto a prueba, les proponemos crear su propio int(). 
# Para lograrlo deben definir una funcion text2number() que reciba como parámetro una variable de tipo string y devuelva un número entero correspondiente a la conversión, tal como funciona int(). 
# Los requisitos que debe cumplir la entrada para ser considerada válida son:

# Al inicio puede contener o no cierta cantidad de espacios " ".
# Luego puede o no tener 1 caracter de signo: "+" ó "-".
# Luego tiene cierta cantidad de caracteres numéricos: entre "0" y "9".
# Por último puede contener o no cierta cantidad de espacios " ".

def string2number(string):
  n_string = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
  n_int = [ 0,   1,   2,   3,   4,   5,   6,   7,   8,   9]

  number = 0
  sign = 1

  i = 0
  while string[i] == " ":
    i += 1
    if i == len(string):
      return None

  if string[i] == "+":
    sign = 1
    i += 1
  if string[i] == "-":
    sign = -1
    i += 1

  if i == len(string):
    return None

  while i < len(string):
    if string[i] in n_string:
      number *= 10
      index = n_string.index( string[i] )
      number += n_int[index]
    elif string[i] != " ":
      return None
    else:
      break
    i += 1

  if i < len(string):
    while string[i] == " ":
      i += 1
      if i == len(string):
        return sign*number
    else:
      return None
  else:
    return sign*number

print(string2number("   +123   ")) #Se espera 123
print(string2number(" 4 5 6 ")) #Se espera None
print(string2number(" -789 ")) #Se espera -789
print(string2number(" - 123 ")) #Se espera None
print(string2number("456")) #Se espera 456