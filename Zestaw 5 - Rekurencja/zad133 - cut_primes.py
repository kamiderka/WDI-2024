"""
Zadanie 133. Proszę napisać funkcję, która jako argument przyjmuje liczbę całkowitą i wypisuje wszystkie
co najmniej dwucyfrowe liczby pierwsze, powstałe poprzez wykreślenie z liczby pierwotnej co najmniej jednej
cyfry
"""

def is_prime(n: int)->bool:
    if n < 2: return False
    i = 2
    while i*i <= n:
        if n%i==0:
            return False
        i+=1

    return True

def cut_primes(stash :int, curr :int, pow :int )->None:
    if stash == 0:
        if is_prime(curr):
            print(curr)
        return

    cut_primes(stash//10, curr, pow)
    cut_primes(stash//10, curr + (stash%10)*pow, pow*10)

n = int(input("Podaj liczbę do pocięcia: "))
cut_primes(n,0, 1)