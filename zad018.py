# Zadanie 18. Nieskończony iloczyn √ wartość 2/π. Proszę napisać program korzystający z tej zależności i wyznaczający wartość π.
from math import sqrt

def calculate_pi(eps=10e-10):
    prev = 0 
    x = sqrt(0.5)
    S = sqrt(0.5)

    while abs(x - prev)>eps:
        prev = x
        x = sqrt(0.5 + 0.5*x)
        S *= x
    return 2/S

print("Pi =", calculate_pi())
