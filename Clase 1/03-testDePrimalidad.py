# Escribir una función que recibe un número y devuelve True si el número es primo y False en caso contrario.
# Mediante un for verificar la primalidad de los numeros del  1  al  20 , es decir, decidir si cada número es primo o no.

def is_primo(number):
  if number == 1:
    return print('El número 1 no es primo.')
  for n in range(2, number):
    if number % n == 0:
      return False
  return True

for n in range(1,20):
  if is_primo(n):
    print('El número',n,'es primo.')
  else:
    print('El número',n,'no es primo.')