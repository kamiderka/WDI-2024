"""============================================
Zadanie 140. Dany jest zestaw odważników T[N]. Napisać funkcję, która sprawdza, czy jest możliwe
odważenie określonej masy. Odważniki można umieszczać tylko na jednej szalce.
============================================"""

def one_scale(T :list[int], target :int, i :int=0, curr_sum :int=0)->bool:
    if curr_sum > target: return False
    if curr_sum == target: return True
    if i == len(T): return False

    if one_scale(T, target, i+1, curr_sum+T[i]): return True    # Take
    if one_scale(T, target, i+1, curr_sum): return True         # Don't take

    return False

assert one_scale([1, 2, 3, 4, 5], 10) == True  # Można uzyskać masę 10 (np. 5 + 3 + 2)
assert one_scale([1, 2, 3, 4, 5], 11) == True  #  można uzyskać masy 11 (5 + 4 + 2)
assert one_scale([2, 5, 6], 8) == True  # Można uzyskać masę 8 (np. 2 + 6)
assert one_scale([1, 3, 5], 4) == True  # Można uzyskać masę 4 (np. 1 + 3)
assert one_scale([5, 7, 10], 4) == False  # Nie można uzyskać masy 4
assert one_scale([2, 4, 6], 7) == False  # Nie można uzyskać masy 7

