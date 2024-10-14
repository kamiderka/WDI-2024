# Zadanie 5. Pierwiastek całkowitoliczbowy z liczby naturalnej to część całkowita z pierwiastka z tej liczby.
# Proszę napisać program obliczający taki pierwiastek korzystając z zależności 1 + 3 + 5 + ... = n^2

from math import isqrt

def zad5(target :int)->int:
    n,curr_sum, curr_a =0,0,1
    while curr_sum <= target:
        n+=1
        curr_sum+=curr_a
        curr_a+=2
    return n-1

n = int(input("Podaj liczbę: "))
print("Pierwiastek całkowitoliczbowy:", zad5(n))

for i in range(1000):
    assert isqrt(i) == zad5(i)
