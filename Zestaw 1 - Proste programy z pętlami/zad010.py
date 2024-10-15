# Zadanie 10. Proszę napisać program sprawdzający czy zadana liczba jest pierwszą.

def zad10(n :int)->bool:
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n%2==0 or n%3==0:
        return False

    i = 3
    while i*i <= n:
        if n%i == 0:
            return False
        i+=2

        if n%i==0:
            return False
        i+=4
    return True

"""
Garek improvements:
1) Sprawdzamy tylko liczby nieparzyste (zaczynamy od i=3, n%2, i+=1)
2) Pomijamy również n%3 

I = T
II = T/2
III = T/3

Na kolosie wystarczy wersja z i**i <= n i normalnymi modulo
"""

n = int(input("Podaj liczbę: "))
print("Is_prime:", zad10(n))
