#Imprimir los primeros n números de la sucesión de Fibonacci.

def fibonacci(n):
  a = 0
  b = 1
  for x in range (n):
    print(a)
    c = a
    a += b
    b = c

fibonacci(10)