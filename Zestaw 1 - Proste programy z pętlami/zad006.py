# Proszę napisać program wyznaczający pierwiastek kwadratowy ze wzoru Newtona.
# X(n+1) = 1/2(X(n) + a/X(n))   

def zad6(target:int, eps=10e-10)->float:
    x1 = 1 
    x2 = (target/x1 + x1) * 0.5
    
    while abs(x2 - x1) > eps:
        x1 = x2
        x2 = (target/x1 + x1) * 0.5

    return x2

n = int(input("Podaj liczbę: "))
print("Pierwiastek:",zad6(n))
