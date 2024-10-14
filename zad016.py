# Zadanie 16. Proszę napisać program wyznaczający najmniejszą wspólną wielokrotność 3 zadanych liczb naturalnych.

def nwd(a :int, b :int)->int:
    while a!=b:
        if a > b:
            a-=b
        else:
            b-=a
    return a 

def nww(a :int, b :int)->int:
    return a*b//nwd(a,b)

a = int(input("Podaj 1. liczbę: "))
b = int(input("Podaj 2. liczbę: "))
c = int(input("Podaj 3. liczbę: "))
print("NWD:", nww(nww(a,b),c))


