"""
Zadanie 101. Napisać funkcję która dla tablicy T[N][N], wypełnionej liczbami całkowitymi, 
zwraca wartość True w przypadku, gdy w każdym wierszu i każdej kolumnie występuje co najmniej jedno 0 oraz 
wartość False w przeciwnym przypadku.
"""

def is_zero_in_rows_and_cols(t :list[list[int]])->bool:

    col_zeros = [False for _ in range(len(t[0]))]
    row_zeros = [False for _ in range(len(t))] 
    
    for y in range(0, len(t)):
        for x in range(0, len(t[0])):
            if t[y][x]==0:
                col_zeros[x] = True
                row_zeros[y] = True

    return all(col_zeros) and all(row_zeros)


# __Testy__:

# Przykład, gdzie każdy wiersz i każda kolumna zawiera co najmniej jedno zero
T1 = [
    [1, 0, 3],
    [4, 5, 0],
    [0, 7, 8]
]
assert is_zero_in_rows_and_cols(T1) == True, "Test 1 nie powiódł się"

# Przykład, gdzie jeden z wierszy nie zawiera zera
T2 = [
    [1, 2, 3],
    [4, 5, 0],
    [0, 7, 8]
]
assert is_zero_in_rows_and_cols(T2) == False, "Test 2 nie powiódł się"

# Przykład, gdzie jedna z kolumn nie zawiera zera
T3 = [
    [1, 0, 3],
    [4, 5, 6],
    [0, 7, 8]
]
assert is_zero_in_rows_and_cols(T3) == False, "Test 3 nie powiódł się"

# Przykład, gdzie zarówno każda kolumna, jak i każdy wiersz zawiera co najmniej jedno zero
T4 = [
    [0, 1, 0],
    [0, 0, 0],
    [0, 0, 0]
]
assert is_zero_in_rows_and_cols(T4) == True, "Test 4 nie powiódł się"

# Przykład, gdzie mamy macierz 1x1 bez zera
T5 = [
    [1]
]
assert is_zero_in_rows_and_cols(T5) == False, "Test 5 nie powiódł się"

# Przykład, gdzie mamy macierz 1x1 z zerem
T6 = [
    [0]
]
assert is_zero_in_rows_and_cols(T6) == True, "Test 6 nie powiódł się"

print("Wszystkie testy zakończone sukcesem.")

