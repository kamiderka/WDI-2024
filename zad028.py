# Zadanie 28. Proszę napisać program wczytujący liczbę naturalną i rozkładający ją na iloczyn 2 liczb o
# najmniejszej różnicy. Na przykład: 30 = 5 ∗ 6, 120 = 10 ∗ 12.

from math import sqrt, floor

def closest_divisors(n :int)->(int,int):
    
    for i in range(floor(sqrt(n)), 1, -1):
        if n%i == 0:
            return (i, n//i)
    return 1,n

n = int(input("Podaj liczbę: "))
print("Najbliższe dzielniki:", str(closest_divisors(n)))

