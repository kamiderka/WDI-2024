""" 
Zadanie 94. Dana jest tablica T[N][N] wypełniona liczbami naturalnymi. Proszę napisać funkcję, która
odpowiada na pytanie, czy istnieje wiersz w tablicy w którym każda z liczb zawiera przynajmniej jedna cyfrę
parzystą.
"""

def has_odd_digits_only(n :int)->bool:
    
    while n > 0:
        if (n%10)%2==0:
            return False
        n//=10
    return True

def check_even_in_rows(t :list[list[int]])->bool:
    for y in range(0,len(t)):
        not_found = True
        for x in range(0, len(t[y])):
            if has_odd_digits_only(t[y][x]):
                not_found = False
                break
        if not_found:
            return True
    return False

# __Testy:__
assert check_even_in_rows([
    [24, 36, 58],
    [135, 24, 57],
    [913, 27, 91]
]) == True  # Pierwszy wiersz spełnia warunek (każda liczba zawiera cyfrę parzystą).

assert check_even_in_rows([
    [135, 57, 79],
    [111, 28, 78],
    [913, 37, 91]
]) == False  # Żaden wiersz nie spełnia warunku (nie wszystkie liczby mają cyfrę parzystą).

assert check_even_in_rows([
    [20, 42, 60],
    [111, 31, 55],
    [52, 78, 24]
]) == True  # Pierwszy i trzeci wiersz spełniają warunek.

assert check_even_in_rows([
    [135, 57, 79],
    [135, 27, 37],
    [913, 35, 91]
]) == False  # Żaden wiersz nie spełnia warunku.

assert check_even_in_rows([
    [42, 56, 82],
    [18, 20, 32],
    [52, 78, 24]
]) == True  # Wszystkie wiersze spełniają warunek.

print("OK!")
