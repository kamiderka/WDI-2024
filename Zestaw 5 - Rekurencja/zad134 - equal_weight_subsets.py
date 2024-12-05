"""
Zadanie 134. ”Waga” liczby jest określona jako ilość różnych czynników pierwszych liczby. Na przykład
waga(1)=0, waga(2)=1, waga(6)=2, waga(30)=3, waga(64)=1. Dana jest tablica T[N] zawierająca liczby
naturalne. Proszę napisać funkcję, która sprawdza czy można elementy tablicy podzielić na 3 podzbiory o
równych wagach. Do funkcji należy przekazać wyłącznie tablicę, funkcja powinna zwrócić wartość typu Bool
"""

def count_prime_divisors(n :int) -> int:
    result = 0

    i = 2
    while i*i <= n:
        if n%i ==0:
            result += 1
            while n%i ==0 and n > 0:
                n//=i
        i+=1

    if n > 1:
        result+=1

    return result

def rek_equal_weight_subset(T :list, i : int=0, s1 :int=0, s2: int=0, s3 :int=0) -> bool:
    if i == len(T):
        return s1 == s2 and s2 == s3

    return bool(rek_equal_weight_subset(T, i+1, s1 + T[i], s2, s3) or
                rek_equal_weight_subset(T, i+1, s1 ,s2 + T[i], s3) or
                rek_equal_weight_subset(T, i + 1, s1, s2, s3+ T[i]))

# Zakładam, że można zniszczyć dane z tablicy T
def equal_weight_subset(N :list)->bool:
    T = [count_prime_divisors(N[i]) for i in range(len(N))]
    return rek_equal_weight_subset(T)

assert equal_weight_subset([1,30, 2, 6, 64, 6]) == True
assert equal_weight_subset([1,30, 2, 6, 64]) == False
