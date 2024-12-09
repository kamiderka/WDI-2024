"""===================================================
Zadanie 139. Liczba dwu-trzy-piątkowa w rozkładzie na czynniki pierwsze nie posiada innych czynników
niż 2, 3, 5. Jedynka też jest taką liczbą. Proszę napisać funkcję rekurencyjną, wypisującą liczby znajdujące
się w przedziale od 1 do N włącznie.
==================================================="""

def rozkładaj_na_czynniki(n):
    czynniki = []
    dzielnik = 2
    while dzielnik * dzielnik <= n:
        while n % dzielnik == 0:
            czynniki.append(dzielnik)
            n //= dzielnik
        dzielnik += 1
    if n > 1:
        czynniki.append(n)
    print(*czynniki)

def gen5(N :int, num :int)->None:
    if num > N: return
    print(num, end="\t")
    rozkładaj_na_czynniki(num)
    gen5(N, num*5)

def gen35(N :int, num :int)->None:
    if num > N: return
    print(num, end="\t")
    rozkładaj_na_czynniki(num)
    gen35(N,num*3)
    gen5(N, num*5)

def gen235(N :int, num :int=1)->None:
    if num > N: return
    print(num, end="\t")
    rozkładaj_na_czynniki(num)
    gen235(N, num*2)
    gen35(N,num*3)
    gen5(N, num*5)

gen235(100)



