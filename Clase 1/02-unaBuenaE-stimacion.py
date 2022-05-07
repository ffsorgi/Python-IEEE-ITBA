#Se pide obtener una aproximación del número e calculando la suma de los primeros 20 términos de la serie de Taylor.

#b = base
def factorial(b):
  amount = 1
  while b != 0:
    amount = amount * b
    b -= 1
  return amount

def e():
  e = 0
  for x in range(20):
    e += (1/factorial(x))
  return e

print(e())