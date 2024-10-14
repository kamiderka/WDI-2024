# Zadanie 15. Proszę napisać program wyznaczający największy wspólny dzielnik 3 zadanych liczb naturalnych.

def nwd(a :int, b :int)->int:
    while a != b:
        if a > b:
            a-=b
        else:
            b-=a
    return a 

a = int(input("Podaj 1. liczbę: "))
b = int(input("Podaj 2. liczbę: "))
c = int(input("Podaj 3. liczbę: "))
print("NWD:", nwd(nwd(a,b),c))
