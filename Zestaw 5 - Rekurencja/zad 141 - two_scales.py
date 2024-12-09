"""============================================
Zadanie 140. Dany jest zestaw odważników T[N]. Napisać funkcję, która sprawdza, czy jest możliwe
odważenie określonej masy. Odważniki można umieszczać tylko na jednej szalce.
============================================"""

def two_scales(T :list[int], target :int, i :int=0, sum1 :int=0, sum2 :int=0)->bool:
    if sum1 > target or sum2 > target: return False
    if sum1 == sum2 and sum2 == target: return True
    if i == len(T): return False

    return (
        two_scales(T, target, i+1, sum1 + T[i], sum2) or
        two_scales(T, target, i + 1, sum1 , sum2 + T[i]) or
        two_scales(T, target, i + 1, sum1, sum2)
    )

# === Testy ===
assert two_scales([1, 2, 3, 4], 5) == True  # Możliwe: 4 na jednej szalce, 1 + 2 + 3 na drugiej
assert two_scales([1, 2, 3], 7) == False  # Nie można uzyskać różnicy 7
assert two_scales([2, 4, 6], 0) == True  # Możliwe, jeśli masy są równo rozdzielone
assert two_scales([2, 5, 10, 3], 10) == True  # Możliwe: np. 10 na jednej, 5 + 2 na drugiej
assert two_scales([3, 3, 3], 1) == False  # Różnica 1 jest niemożliwa
print("OK!")
