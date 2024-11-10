"""
Zadanie 97. Dane są dwie tablice mogące pomieścić taką samą liczbę elementów: T1[N][N] i T2[M], gdzie
M=N*N. W każdym wierszu tablicy T1 znajdują się uporządkowane rosnąco (w obrębie wiersza) liczby
naturalne. Proszę napisać funkcję przepisującą wszystkie singletony (liczby występujące dokładnie raz) z
tablicy T1 do T2, tak aby liczby w tablicy T2 były uporządkowane rosnąco. Pozostałe elementy tablicy T2
powinny zawierać zera.
"""

from math import inf


def find_min_stage(t :list[list], stage :list)->int:
    mini = 0
    for y in range(1, len(stage)):
        if t[y][stage[y]] < t[mini][stage[mini]]:
            mini = y
    return mini

def find_singletons(t1 :list[list], t2 : list)->list:
    n = len(t1[0])
    t2_ind = 0
    stage = [0 for _ in range(len(t1))]
    

    curr_y = find_min_stage(t1, stage)
    prev = t1[curr_y][stage[curr_y]]
    flag = True
    if stage[curr_y] == n - 1: 
        t1[curr_y][stage[curr_y]] = inf
    else:
        stage[curr_y]+=1
    
    for _ in range(1, len(t2)):
        curr_y = find_min_stage(t1,stage)
        curr = t1[curr_y][stage[curr_y]]
        if curr != prev:
            if flag:
                t2[t2_ind] = prev
                t2_ind+=1
            else:
                flag = True
            prev = curr
        else:
            flag = False

        if stage[curr_y] == n - 1: 
            t1[curr_y][stage[curr_y]] = inf
        else:
            stage[curr_y]+=1

    if flag:
        t2[t2_ind] = prev

    return t2

# Test 1: Przykład z różnymi liczbami, gdzie niektóre występują więcej niż raz
t1 = [
    [1, 3, 5],
    [2, 4, 5],
    [7, 8, 9]
]
t2 = [0] * 9
find_singletons(t1, t2)
assert t2 == [1, 2, 3, 4, 7, 8, 9, 0, 0 ], f"Test 1 failed: {t2}"

# Test 2: Wszystkie liczby w T1 są unikalne i uporządkowane rosnąco
t1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
t2 = [0] * 9
find_singletons(t1, t2)
assert t2 == [1, 2, 3, 4, 5, 6, 7, 8, 9], f"Test 2 failed: {t2}"

# Test 3: Wszystkie liczby w T1 są takie same, więc nie ma singletonów
t1 = [
    [5, 5, 5],
    [5, 5, 5],
    [5, 5, 5]
]
t2 = [0] * 9
find_singletons(t1, t2)
assert t2 == [0, 0, 0, 0, 0, 0, 0, 0, 0], f"Test 3 failed: {t2}"

# Test 4: T1 zawiera mieszane wartości z pojedynczymi singletonami, wiersze rosnąco
t1 = [
    [1, 2, 2],
    [3, 4, 4],
    [5, 6, 6]
]
t2 = [0] * 9
find_singletons(t1, t2)
assert t2 == [1, 3, 5, 0, 0, 0, 0, 0, 0], f"Test 4 failed: {t2}"

# Test 5: Minimalny przypadek z tablicą 1x1
t1 = [
    [42]
]
t2 = [0]
find_singletons(t1, t2)
assert t2 == [42], f"Test 5 failed: {t2}"

# Test 6: Tablica 2x2 z unikalnymi elementami rosnącymi w wierszach
t1 = [
    [1, 3],
    [2, 4]
]
t2 = [0] * 4
find_singletons(t1, t2)
assert t2 == [1, 2, 3, 4], f"Test 6 failed: {t2}"

# Test 7: T1 z wartościami rosnącymi i powtarzającymi się
t1 = [
    [1, 2, 3],
    [3, 4, 5],
    [5, 6, 7]
]
t2 = [0] * 9
find_singletons(t1, t2)
assert t2 == [1, 2, 4, 6, 7, 0, 0, 0, 0], f"Test 7 failed: {t2}"

print("All tests passed.")

