# Zadanie 25. Proszę napisać program wczytujący liczbę naturalną i odpowiadający na pytanie, czy liczba
# ta jest iloczynem dowolnych dwóch wyrazów ciągu Fibonacciego.
from math import sqrt

def is_fibonacci_product(n :int)->bool:
    a,b=1,1
    occur = set([1])
    while a <= sqrt(n):
        if n/a in occur:
            return True
        occur.add(a)
        c = a+b
        a = b
        b = c
    return False        

"""
Garek content: 
1) Garek używa funkcji is_fib(n), która sprawdza oczywiste
2) a <= n -> a <= sqrt(n)
"""
n = int(input("Podaj N: "))
print("Czy iloczyn Fibonacciego:", is_fibonacci_product(n))
