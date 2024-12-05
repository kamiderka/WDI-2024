"""
Zadanie 132. Korzystając z zależności: N(n,k) = N(n−1, k-1) + N(n-1, k)
proszę napisać funkcję obliczającą wartość symbolu Newtona dla argumentów n i k
"""

def newton(n :int, k: int) -> int:
    if k==0 or k==n: return 1
    if k==1 or k==n-1: return n
    return newton(n-1, k-1) + newton(n-1, k)

assert newton(17, 6) == 12376

print("OK!")