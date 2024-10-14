# Zadanie 3. Proszę znaleźć wyrazy początkowe ciągu zamiast 1,1 o najmniejszej sumie, aby w ciągu
# analogicznym do ciągu Fibonacciego wystąpił wyraz równy numerowi bieżącego roku.

def fib(a:int, b:int, year:int) -> bool:
    while a<year:
        if a == year:
            return True
        c = a + b
        a = b
        b = c
    return a == year


def zad3_bf(year: int) -> tuple: 
    min_sum = year
    min_i = [1,year-1]
    for j in range(2,year//2+1):
        for i in range(1, j+1):
            if fib(i,j,year) and min_sum > i + j:
                min_sum = i + j
                min_i = [i,j]
    a,b=min_i
    while a<=year:
        print(a)
        c = a + b
        a = b
        b = c
    
    return tuple(min_i)

n = int(input("Podaj rok: "))
print(zad3_bf(n))
