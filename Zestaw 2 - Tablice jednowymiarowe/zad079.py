# Zadanie 79. Dana jest N-elementowa tablica t zawierająca liczby naturalne mniejsze od 1000. 
# Proszę napisać funkcję, która zwraca długość najdłuższego, spójnego fragmentu tablicy, 
# dla którego w iloczynie jego elementów każdy czynniki pierwszy występuje co najwyżej raz.
# Na przykład dla tablicy t=[2,23,33,35,7,4,6,7,5,11,13,22] wynikiem jest wartość 5.
from math import isqrt

def insert_prim_factors(t :list, n :int)->int:
    k = 2
    while k <= isqrt(n):
        if n%k==0:
            if t[k] == True:
                return False
            t[k] = True
            n//=k
            if n%k == 0:
                return False
        k+=1
    if n > 1:  # Jeśli n jest liczbą pierwszą
        if t[n]:
            return False
        t[n] = True

    return True

def longest_unique_primfactor_subsequence(t: list)->int:
    longest = 0
    for i in range(0,len(t)):
        occur = [False for _ in range(1000)]
        ok = insert_prim_factors(occur, t[i])
        j = i+1
        while ok and j < len(t):
            ok = insert_prim_factors(occur, t[j])
            j += 1
        longest = max(longest, j-i - int(not ok))
    return longest

assert longest_unique_primfactor_subsequence([2,23,33,35,7,4,6,7,5,11,13,22]) == 5
assert longest_unique_primfactor_subsequence([2,3,5,7,11]) == 5 
assert longest_unique_primfactor_subsequence([2, 5, 4, 6, 7, 33, 22]) == 2

print("OK!")

