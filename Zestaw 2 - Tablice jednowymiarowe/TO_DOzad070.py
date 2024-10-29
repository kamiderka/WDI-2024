# Zadanie 70. Napisz funkcję, która dla N-elementowej tablicy T wypełnionej liczbami naturalnym 
# wyznacza długość najdłuższego, spójnego podciągu geometrycznego


# Obsługa dzielenia przez zero (nie chce mi się teraz)
def len_of_longest_geo_progression(nums :lits)->int:
    if len(nums)<2 and not (0 in nums):
        return 0

    max_len =2
    counter = 0
    for end in range(2,len(nums)):

        
