"""
Zadanie 87. Dana jest N-elementowa tablica T, zawierająca liczby. Proszę napisać funkcję, która zwróci
indeks największej liczby, która jest iloczynem wszystkich liczb pierwszych leżących w tablicy na indeksach
mniejszych od niej, lub None jeżeli taka liczba nie istnieje.
"""

def is_prime(n :int)->bool:
    if n < 2:
        return False
    i=2
    while i*i<=n:
        if n%i==0:
            return False
        i+=1
    return True

def biggest_prime_product(t: list)->int | None:
    index = None
    best = 1
    curr = t[0] if is_prime(t[0]) else 1
    for i in range(1, len(t)):
        if t[i] == curr and curr > best:
            best = curr
            index = i
        if is_prime(t[i]):
            curr *= t[i]
    return index

# __Testy__: 
assert biggest_prime_product([2,2,4,7,8,28,2]) == 5
assert biggest_prime_product([1,1,1,1,1,1,1]) == None
assert biggest_prime_product([2,2,4,7,8,27,2]) == 2

print("OK!")
