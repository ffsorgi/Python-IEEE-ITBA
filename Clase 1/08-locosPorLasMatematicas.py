# Aprovechando el descubrimiento del matemático indio Sriniviasa Ramanujan (1910) podemos emplear nuestro propio aproximador de pi.

def factorial(n):
  return 1 if n<=1 else n*factorial(n-1)

def piAproximado(r):
    a = 2*2**(1/2)/9801
    b = 0
    for k in range(r):
        b += factorial(4*k) /factorial(k)**4 *(1103+26390*k)/396**(4*k)

    return 1/(a*b)

print('Pi aproximado es:',piAproximado(10))
