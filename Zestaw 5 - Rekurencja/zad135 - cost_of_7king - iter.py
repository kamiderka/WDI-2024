"""
Zadanie 135. Szachownica jest reprezentowana przez tablicę T[8][8] wypełnioną liczbami naturalnymi
zawierającymi koszt przebywania na danym polu szachownicy. Król szachowy znajduje się w wierszu 0 i
kolumnie k. Król musi w dokładnie 7 ruchach dotrzeć do wiersza 7. Proszę napisać funkcję, która wyznaczy
minimalny koszt przejścia króla. Do funkcji należy przekazać tablicę t oraz startową kolumnę k. Koszt
przebywania na polu startowym i ostatnim także wliczamy do kosztu przejść
"""

def cost_of_7king(T :list[list[int]], k :int) -> int:

    for y in range(len(T)-2, 0, -1):
        for x in range(len(T)):
            point = T[y+1][x]
            if x > 0:
                point = min(point, T[y+1][x-1])
            if x < len(T)-1:
                point = min(point, T[y+1][x+1])

            T[y][x] += point

    point = T[1][k]
    if k > 0:
        point = min(point, T[1][k - 1])
    if k < len(T) - 1:
        point = min(point, T[1][k + 1])

    return T[0][k] + point


# Testy
T1 = [
    [1, 2, 3, 4, 5, 6, 7, 8],
    [8, 7, 6, 5, 4, 3, 2, 1],
    [1, 2, 3, 4, 5, 6, 7, 8],
    [8, 7, 6, 5, 4, 3, 2, 1],
    [1, 2, 3, 4, 5, 6, 7, 8],
    [8, 7, 6, 5, 4, 3, 2, 1],
    [1, 2, 3, 4, 5, 6, 7, 8],
    [8, 7, 6, 5, 4, 3, 2, 1]
]
# Test 1: Start w kolumnie 0
assert cost_of_7king(T1, 0) == 32, "Test 1 failed"

T1 = [
    [1, 2, 3, 4, 5, 6, 7, 8],
    [8, 7, 6, 5, 4, 3, 2, 1],
    [1, 2, 3, 4, 5, 6, 7, 8],
    [8, 7, 6, 5, 4, 3, 2, 1],
    [1, 2, 3, 4, 5, 6, 7, 8],
    [8, 7, 6, 5, 4, 3, 2, 1],
    [1, 2, 3, 4, 5, 6, 7, 8],
    [8, 7, 6, 5, 4, 3, 2, 1]
]
# Test 2: Start w kolumnie 7
assert cost_of_7king(T1, 7) == 33, "Test 2 failed"

T2 = [
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1]
]

# Test 3: Szachownica z kosztami równymi 1
assert cost_of_7king(T2, 3) == 8, "Test 3 failed"

T3 = [
    [10, 20, 30, 40, 50, 60, 70, 80],
    [80, 70, 60, 50, 40, 30, 20, 10],
    [10, 20, 30, 40, 50, 60, 70, 80],
    [80, 70, 60, 50, 40, 30, 20, 10],
    [10, 20, 30, 40, 50, 60, 70, 80],
    [80, 70, 60, 50, 40, 30, 20, 10],
    [10, 20, 30, 40, 50, 60, 70, 80],
    [80, 70, 60, 50, 40, 30, 20, 10]
]

# Test 4: Start w kolumnie 0 z różnymi kosztami
assert cost_of_7king(T3, 0) == 320, "Test 4 failed"


print("All tests passed!")
