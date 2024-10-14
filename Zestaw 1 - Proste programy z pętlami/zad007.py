# Zadanie 7. Proszę zmodyfikować wzór Newtona aby program z poprzedniego zadania obliczał pierwiastek stopnia 3.
# Tip: Oblicz ze wzoru metody Newtona (tej z pochodną)

def zad7(target :int, eps=10e-10)->float:
    x1 = 1
    x2 = (2*x1 + target/x1**2)/3

    while abs(x2-x1) > eps:
        x1 = x2 
        x2 = (2*x1 + target/x1**2)/3

    return x2

n = int(input("Podaj liczbę: "))
print("Cube root:", zad7(n))
