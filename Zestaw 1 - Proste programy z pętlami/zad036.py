# Zadanie 36. Proszę napisać program wyliczający 
# pierwiastek równania x**x = 2020 metodą stycznych

from math import log,sqrt, sin, cos

def f(x_x :float, a :float)->float:
    return x_x-a

def df(x:float, x_x:float)->float:
    return x_x*(1+log(x))

# Metoda algerbaiczna, prawdę mówiąc, nie jestem do niej przekonany
# Nieskuteczna dla większych liczb, wynik zwraca prawidłowy
def estimate_xpower_x(a :float, eps=10e-10)->float:
    prev = 0
    x = sqrt(a)
    while abs(x - prev) > eps:
        prev = x
        x_x = x**x
        x = x - f(x_x, a)/df(x,x_x)
    return x

a = int(input("Podaj szukaną x**x: "))
print("Szacowany pierwiastek (metoda algebraiczna):", estimate_xpower_x(a))
