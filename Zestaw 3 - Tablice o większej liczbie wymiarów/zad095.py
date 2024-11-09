# Zadanie 95. Dana jest tablica T[N][N] wypełniona liczbami naturalnymi. Proszę napisać funkcję, która
# zwraca wiersz i kolumnę dowolnego elementu, dla którego iloraz sumy elementów w kolumnie w którym leży
# element do sumy elementów wiersza w którym leży element jest największa.

def max_quotient_col_to_row_sum(t : list[list[int]])->tuple[int,int]:

    col_max, col_ind = float('-inf'), -1
    for x in range(0, len(t[0])):
        curr_sum = 0
        for y in range(0, len(t)):
            curr_sum += t[y][x]
        if curr_sum > col_max:
            col_max = curr_sum
            col_ind = x

    row_min, row_ind = float('inf'), -1
    for y in range(0, len(t)):
        curr_sum = sum(t[y])
        if curr_sum != 0 and curr_sum < row_min:
            row_min = curr_sum
            row_ind = y 
    
    if row_ind == -1 or col_ind == - 1:
        return -1, -1

    return row_ind, col_ind




# __ Testy: __
assert max_quotient_col_to_row_sum([
    [5]
]) == (0, 0)  # Tylko jeden element, więc wynik to jego współrzędne (0, 0).

# Testy dla większych tablic
assert max_quotient_col_to_row_sum([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]) == (0, 2)  

assert max_quotient_col_to_row_sum([
    [10, 20, 30],
    [5, 15, 25],
    [35, 45, 55]
]) == (1, 2)  

assert max_quotient_col_to_row_sum([
    [0, 1, 2],
    [0, 0, 3],
    [4, 5, 6]
]) == (0, 2)  

assert max_quotient_col_to_row_sum([
    [4, -4, 0],
    [-4, 4, 0],
    [0, 0, 0]
]) == (-1, -1)

print("OK!")

