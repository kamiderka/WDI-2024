"""
Zadanie 93. Dana jest tablica T[N][N] wypełniona liczbami naturalnymi. Proszę napisać funkcję, która
odpowiada na pytanie, czy w każdym wierszu tablicy występuje co najmniej jedna liczba złożona wyłącznie
z nieparzystych cyfr.
"""

def are_odd_digits_only(n :int)->bool:
    while n>0:
        if (n%10)%2 == 0:
            return False
        n//=10
    return True

def check_odd_numbers_in_row(t):
    
    for y in range(0,len(t)):
        found = False
        for x in range(0, len(t[y])):
            if are_odd_digits_only(t[y][x]):
                found = True
                break
        if not found:
            return False

    return True


# __Testy__:
assert check_odd_numbers_in_row([
    [135, 24, 57],
    [333, 26, 78],
    [913, 27, 91]
]) == True  # Każdy wiersz zawiera liczbę z nieparzystymi cyframi (135, 333, 913).

assert check_odd_numbers_in_row([
    [135, 24, 57],
    [246, 28, 78],
    [913, 27, 91]
]) == False  # Drugi wiersz nie ma liczby złożonej wyłącznie z nieparzystych cyfr.

assert check_odd_numbers_in_row([
    [11, 33, 77],
    [99, 111, 55],
    [555, 777, 333]
]) == True  # Wszystkie liczby mają wyłącznie nieparzyste cyfry.

assert check_odd_numbers_in_row([
    [10, 22, 30],
    [246, 48, 70],
    [913, 27, 91]
]) == False  # Pierwszy i drugi wiersz nie mają liczby z wyłącznie nieparzystymi cyframi.

assert check_odd_numbers_in_row([
    [137, 245, 753],
    [135, 246, 357],
    [531, 727, 91]
]) == True  # W każdym wierszu jest liczba z wyłącznie nieparzystymi cyframi (137, 135, 727).

print("OK!")
