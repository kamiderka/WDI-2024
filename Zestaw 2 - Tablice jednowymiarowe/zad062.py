# Zadanie 62. Napisać program generujący i wypisujący liczby pierwsze mniejsze od N metodą Sita Eratostenesa.

from math import isqrt


def erastothenes_sieve(n :int)->None:
    sieve = [True]*(n+1)
    print(2)
    for i in range(3, len(sieve), 2):

        if sieve[i]:
            print(i)
            
            j = 2*i
            while j<=n:
                sieve[j]=False
                j+=i

def sito_garka(n:int)->list:
    t = [True for _ in range(n+1)]
    t[0],t[1] = False,False
    for i in range(2, isqrt(n)+1):
        if t[i]:
            for j in range(i*2, n+1, i):
                t[j] = False
    return t


n = int(input("Podaj granicę sita: "))
erastothenes_sieve(n)

"""
___Garek Content___:





"""
