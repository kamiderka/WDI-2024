# Zadanie 69. Napisać funkcję, która dla N-elementowej tablicy T wypełnionej liczbami naturalnym
# wyznacza długość najdłuższego, spójnego podciągu arytmetycznego.

def len_of_longest_arythmetic_subsequence(nums :list)->int:
    if len(nums)<2:
        return -1

    max_len = 0
    beg = 0
    r = nums[1]-nums[0]
    for end in range(1,len(nums)):
        if nums[end-1]+r != nums[end]:
            max_len = max(end-beg-1, max_len)
            r = nums[end]-nums[end-1]
            beg = end-1  # ciąg zaczyna się na nums[end-1]
    max_len=max(end-beg,max_len)
    return max_len+1

print(len_of_longest_arythmetic_subsequence([1,2,3,1,2,3,4,5,1,2,3,4,5,6]))
# __Testy__:
assert len_of_longest_arythmetic_subsequence([1,2,3,4,5,6,7,8,2,4,6,8]) == 8
assert len_of_longest_arythmetic_subsequence([1,2,3,1,2,3,4,5,1,2,3,4,5,6]) == 6
assert len_of_longest_arythmetic_subsequence([1]) == -1
assert len_of_longest_arythmetic_subsequence([1,3,2,4,3,4,3,4,3]) == 2
assert len_of_longest_arythmetic_subsequence([-1,-2,-3,-4,-5]) == 5
assert len_of_longest_arythmetic_subsequence([4,1122]) == 2
print("Ok!")
