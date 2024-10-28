# Zadanie 75. Mamy zdefiniowaną n-elementową tablicę liczb całkowitych. Proszę napisać funkcję zwracającą wartość typu bool oznaczającą, 
# czy w tablicy istnieje dokładnie jeden element najmniejszy i dokładnie jeden element największy 
# (liczba elementów najmniejszych oznacza liczbę takich elementów o tej samej wartości).

def has_exactly_one_largest_and_smallest_number(nums :list)->bool:
    min,     max     = float('inf'),float('-inf')
    dup_min, dup_max = False, False

    for num in nums:
        if num >= max:
            dup_max = num == max
            max = num
        if num <= min:
            dup_min = num == min
            min = num

    return not (dup_min or dup_max)

# __Testy__:
assert has_exactly_one_largest_and_smallest_number([1]) == True
assert has_exactly_one_largest_and_smallest_number([1,1]) == False
assert has_exactly_one_largest_and_smallest_number([1,2]) == True
assert has_exactly_one_largest_and_smallest_number([1,1,1,1,2]) == False
assert has_exactly_one_largest_and_smallest_number([1,2,3,4,5,6,7,8]) == True
assert has_exactly_one_largest_and_smallest_number([1,2,3,1,5,6,7,8]) == False

