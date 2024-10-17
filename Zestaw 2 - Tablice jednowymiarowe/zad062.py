# Zadanie 62. Napisać program generujący i wypisujący liczby pierwsze mniejsze od N metodą Sita Eratostenesa.

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

n = int(input("Podaj granicę sita: "))
erastothenes_sieve(n)
