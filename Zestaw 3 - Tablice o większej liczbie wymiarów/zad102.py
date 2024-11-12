""""
Zadanie 102. Dwie liczby naturalne są „przyjaciółkami jeżeli zbiory cyfr z których zbudowane są liczby
są identyczne. Na przykład: 123 i 321, 211 i 122, 35 3553. Dana jest tablica T[N][N] wypełniona liczbami
naturalnymi. Proszę napisać funkcję, która dla tablicy T zwraca ile elementów tablicy sąsiaduje wyłącznie z
przyjaciółkami
"""

def are_friends(a :int, b :int)->bool:
    digits_a = [False] * 10
    digits_b = [False] * 10

    while a > 0:
        digit = a % 10
        digits_a[digit] = True
        a //= 10

    while b > 0:
        digit = b % 10
        digits_b[digit] = True
        b //= 10

    return digits_a == digits_b

def has_friendly_neighbours(t:list[list[int]], x :int, y :int)->bool:
    a = t[y][x]

    if x > 0 and not are_friends(a, t[y][x-1]):
        return False

    if y > 0 and not are_friends(a, t[y-1][x]):
        return False
    
    if x < len(t)-1 and not are_friends(a, t[y][x+1]):
        return False
    
    if y < len(t)-1 and not are_friends(a, t[y+1][x]):
        return False
    
    return True

def count_friendly_neighbours(t :list[list[int]])->int:
    counter = 0

    for y in range(0, len(t)):
        for x in range(0, len(t)):
            if has_friendly_neighbours(t, x, y):
                counter+=1
    return counter

# __Testy__:

# Test 1: Tablica 3x3 z sąsiadującymi liczbami-przyjaciółkami
T1 = [
    [123, 321, 132],
    [213, 231, 312],
    [312, 123, 321]
]
assert count_friendly_neighbours(T1) == 9, "Test 1 nie powiódł się"

# Test 2: Tablica 3x3 z niektórymi liczbami nie będącymi przyjaciółkami
T2 = [
    [123, 45, 123],
    [321, 231, 231],
    [132, 54, 123]
]
assert count_friendly_neighbours(T2) == 2, "Test 2 nie powiódł się"

# Test 3: Tablica 2x2, w której wszystkie liczby są przyjaciółkami
T3 = [
    [112, 211],
    [121, 211]
]
assert count_friendly_neighbours(T3) == 4, "Test 3 nie powiódł się"

# Test 4: Tablica 2x2 bez żadnych przyjaciół
T4 = [
    [12, 34],
    [56, 78]
]
assert count_friendly_neighbours(T4) == 0, "Test 4 nie powiódł się"

# Test 5: Tablica 3x3, niektóre elementy mają tylko jednego sąsiada
T5 = [
    [11, 11, 12],
    [13, 11, 21],
    [31, 41, 51]
]
assert count_friendly_neighbours(T5) == 0, "Test 5 nie powiódł się"

print("Wszystkie testy zakończone sukcesem.")

