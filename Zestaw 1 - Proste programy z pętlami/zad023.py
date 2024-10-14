# Zadanie 23. Dane są ciągi: An+1 = sqrt(An ∗ Bn) oraz Bn+1 =(An + Bn)/2.0. 
# Ciągi te są zbieżne do wspólnej granicy nazywanej średnią arytmetyczno-geometryczną.
# Proszę napisać program wyznaczający średnią arytmetyczno-geometryczną dwóch liczb naturalnych.
from math import sqrt

def geometrical_mean(a1 :int, b1 :int, eps=10e-10)->float:
    if a1 < 0 or b1 < 0:
        return float('nan')
    prev_a, prev_b = a1,b1
    a,b=prev_a,prev_b
    while abs(a - b) > eps:
        a = sqrt(prev_a*prev_b)
        b = (prev_a + prev_b)/2
        prev_a, prev_b = a,b

    return a

a = int(input("Podaj a: "))
b = int(input("Podaj b: "))
print("Średnia arytmetyczno-geometryczna:", geometrical_mean(a,b))
