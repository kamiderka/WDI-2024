"""
Zadanie 100. Dana jest tablica T[N][N] wypełniona liczbami naturalnymi. Proszę napisać funkcję, która
w poszukuje w tablicy kwadratu o liczbie pól będącej liczbą nieparzystą większą od 1, którego iloczyn 4 pól
narożnych wynosi k. Do funkcji należy przekazać tablicę i wartość k. Funkcja powinna zwrócić informacje
czy udało się znaleźć kwadrat oraz współrzędne (wiersz, kolumna) środka kwadratu.
"""

def calc_product(t :list[list[int]], x :int, y :int, d :int)->int:
    return t[y][x]*t[y][x-d]*t[y-d][x-d]*t[y-d][x]


def product_square(t :list[list[int]], product :int)->tuple[bool,tuple[int,int]|None]:
    
    for d in range(2, len(t), 2):
        for y in range(2, len(t)):
            for x in range(2,len(t)):
                if product%t[y][x]==0 and calc_product(t, x, y, d) == product:
                    return (True, (x-(d)//2, y - (d)//2))
    return (False,None)


# __Testy__:
# Test 1: Kwadrat 3x3 z iloczynem narożników równym 24
T1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 4]
]
k1 = 84  # 1 * 3 * 7 * 4 = 84
assert product_square(T1, k1) == (True, (1, 1)), "Test 1 nie powiódł się"

# Test 2: Kwadrat 3x3 bez pasującego iloczynu
T2 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
k2 = 24  # Brak kwadratu o takim iloczynie narożników
assert product_square(T2, k2) == (False, None), "Test 2 nie powiódł się"

# Test 3: Kwadrat 5x5 z iloczynem narożników równym 81
T3 = [
    [1, 1, 1, 1, 3],
    [1, 2, 2, 2, 1],
    [3, 2, 9, 2, 1],
    [1, 2, 2, 2, 1],
    [3, 1, 1, 1, 1]
]
k3 = 81  # 3 * 3 * 3 * 3 = 81
assert product_square(T3, k3) == (True, (1, 3)), "Test 3 nie powiódł się"

# Test 4: Kwadrat 3x3 z iloczynem równym 64, ale większy kwadrat również istnieje
T4 = [
    [2, 1, 2, 1, 2],
    [1, 4, 1, 4, 1],
    [2, 1, 2, 1, 2],
    [1, 4, 1, 4, 1],
    [2, 1, 2, 1, 2]
]
k4 = 16  # Iloczyn narożników w centralnym 3x3: 2 * 2 * 2 * 2 = 16
assert product_square(T4, k4) == (True, (1, 1)), "Test 4 nie powiódł się"

# Test 5: Macierz 1x1, brak kwadratów o nieparzystej liczbie pól większej niż 1
T5 = [
    [1]
]
k5 = 1
assert product_square(T5, k5) == (False, None), "Test 5 nie powiódł się"

print("Wszystkie testy zakończone sukcesem.")

