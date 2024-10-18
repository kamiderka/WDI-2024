# Zadanie 68. Napisać funkcję, która dla N-elementowej tablicy T wypełnionej liczbami naturalnym 
# wyznacza długość najdłuższego, spójnego podciągu rosnącego.
def len_of_longest_subsequence(nums :list)->int:
    if not nums:
        return 0
    if len(nums) == 1:
        return 1

    max_len=0
    beg = 0
    for end in range(1, len(nums)):
        if not (nums[end-1] < nums[end]):
            max_len = max(end-beg-1, max_len)
            beg = end
    max_len = max(end-beg, max_len)
    return max_len+1

# ___Testy___
assert len_of_longest_subsequence([1,2,3,4,5,6,7,8,9]) == 9
assert len_of_longest_subsequence([1,2,3,4,0,1,2,3,4,5,0,0]) == 6
assert len_of_longest_subsequence([7,6,5,4,3,2,1]) == 1
assert len_of_longest_subsequence([1,1,1,1,1]) == 1
assert len_of_longest_subsequence([]) == 0
assert len_of_longest_subsequence([3123]) == 1
assert len_of_longest_subsequence([1,2]) == 2

print("OK!")
