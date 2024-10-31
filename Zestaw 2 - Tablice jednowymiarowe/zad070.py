# Zadanie 70. Napisz funkcję, która dla N-elementowej tablicy T wypełnionej liczbami naturalnym 
# wyznacza długość najdłuższego, spójnego podciągu geometrycznego


# Przyda się obsługa obsługa dzielenia przez zero
def len_of_longest_geo_progression(t :list)->int:
    if len(t)<2:
        return 0 

    best_length = 2
    counter = 2 
    q = t[1]/t[0]
    for i in range(2,len(t)):
        if t[i]/t[i-1] == q:
            counter += 1 
        else:
            best_length = max(best_length, counter)
            counter = 2
            q = t[i]/t[i-1]
    return max(best_length,counter)

# __Testy__:
assert len_of_longest_geo_progression([1,2,4,8,4,2, 1, 16, 16]) == 4
assert len_of_longest_geo_progression([1,1]) == 2
assert len_of_longest_geo_progression([0]) == 0
assert len_of_longest_geo_progression([3,3,3,3,3,3]) == 6
assert len_of_longest_geo_progression([1,3,9,81,729, 6561]) == 4
assert len_of_longest_geo_progression([1,3,9,81,729, 6561, 4, 5]) == 4

print("OK!")
