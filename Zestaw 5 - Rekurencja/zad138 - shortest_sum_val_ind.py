"""==============================================
Zadanie 138. Dana jest tablica T[N]. Proszę napisać funkcję, która znajdzie niepusty, najmniejszy (w
sensie liczebności) podzbiór elementów tablicy, dla którego suma elementów jest równa sumie indeksów
tych elementów. Do funkcji należy przekazać tablicę, funkcja powinna zwrócić sumę elementów znalezionego
podzbioru. Na przykład dla tablicy: [ 1,7,3,5,11,2 ] rozwiązaniem jest liczba 10.
=============================================="""

# Dla wygody użytkownika i programisty zwraca tupla z długością i sumą, na kolosie lepiej tak nie robić
def shortest_sum_val(T :list[int], i :int=0,  sum_ind :int=0, sum_val :int=0, length :int=0 ) -> tuple[int|float,int|None]:
    if i == len(T):
        if length != 0 and sum_ind == sum_val:
            return (length, sum_val)
        return (float('inf'),None)

    take = shortest_sum_val(T, i+1, sum_ind + i, sum_val + T[i], length+1)
    notake = shortest_sum_val(T, i+1, sum_ind , sum_val , length)

    if take[0]<notake[0]:
        return take
    return notake

print(shortest_sum_val([ 1,7,3,5,11,2]))



