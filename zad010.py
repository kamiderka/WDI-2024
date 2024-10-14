# Zadanie 10. Proszę napisać program sprawdzający czy zadana liczba jest pierwszą.

def zad10(n :int)->bool:
    if n < 2:
        return False
    i = 2
    while i*i <= n:
        if n % i == 0:
            return False
        i+=1
    return True

n = int(input("Podaj liczbę: "))
print("Is_prime:", zad10(n))
