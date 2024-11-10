"""
Zadanie 98. Dane są dwie tablice mogące pomieścić taką samą liczbę elementów: T1[N][N] i T2[M], gdzie
M=N*N. W każdym wierszu tablicy T1 znajdują się uporządkowane niemalejąco (w obrębie wiersza) liczby
naturalne. Proszę napisać funkcję przepisującą wszystkie liczby z tablicy T1 do T2, tak aby liczby w tablicy
T2 były uporządkowane niemalejąco.
"""
from math import inf



def find_min_stage_ind(t:list[list[int]], stage :list)->int:
    mini = 0
    for y in range(1, len(t)):
        if t[y][stage[y]] < t[mini][stage[mini]]:
            mini = y
    return mini

def merge_sorted_matrix(t1 :list[list[int]], t2 :list)->list:
    stage = [0 for _ in range(len(t1))]
    n = len(t1[0])
    for i in range(len(t2)):
        curr_y = find_min_stage_ind(t1, stage)
        t2[i] = t1[curr_y][stage[curr_y]]
        if stage[curr_y] == n-1:
            t1[curr_y][stage[curr_y]] = inf
        else:
            stage[curr_y]+=1
    return t2


# Test 1: Tablica 3x3, liczby w T1 są już posortowane niemalejąco w wierszach
t1 = [
    [1, 3, 5],
    [2, 4, 6],
    [7, 8, 9]
]
t2 = [0] * 9
merge_sorted_matrix(t1, t2)
assert t2 == [1, 2, 3, 4, 5, 6, 7, 8, 9], f"Test 1 failed: {t2}"

# Test 2: Wszystkie liczby w T1 są takie same
t1 = [
    [5, 5, 5],
    [5, 5, 5],
    [5, 5, 5]
]
t2 = [0] * 9
merge_sorted_matrix(t1, t2)
assert t2 == [5, 5, 5, 5, 5, 5, 5, 5, 5], f"Test 2 failed: {t2}"

# Test 5: Minimalny przypadek z tablicą 1x1
t1 = [
    [42]
]
t2 = [0]
merge_sorted_matrix(t1, t2)
assert t2 == [42], f"Test 5 failed: {t2}"

# Test 6: Tablica 2x2 z elementami posortowanymi w kolumnach
t1 = [
    [1, 3],
    [2, 4]
]
t2 = [0] * 4
merge_sorted_matrix(t1, t2)
assert t2 == [1, 2, 3, 4], f"Test 6 failed: {t2}"

# Test 7: T1 z wartościami ujemnymi
t1 = [
    [-5, -3, -1],
    [-4, 0, 2],
    [1, 3, 5]
]
t2 = [0] * 9
merge_sorted_matrix(t1, t2)
assert t2 == [-5, -4, -3, -1, 0, 1, 2, 3, 5], f"Test 7 failed: {t2}"

print("OK!")
