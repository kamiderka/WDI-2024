# Zadanie 69. Napisać funkcję, która dla N-elementowej tablicy T wypełnionej liczbami naturalnym
# wyznacza długość najdłuższego, spójnego podciągu arytmetycznego.

def len_of_longest_arythmetic_subsequence(nums :list)->int:
    if len(nums)<2:
        return len(nums)

    max_len = 0
    beg = 0
    while 
