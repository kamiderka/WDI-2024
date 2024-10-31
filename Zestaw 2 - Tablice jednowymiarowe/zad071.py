# Zadanie 71. Proszę napisać program, który wypełnia N-elementową tablicę T pseudolosowymi liczbami
# nieparzystymi z zakresu [1..99], a następnie wyznacza i wypisuje różnicę pomiędzy długością najdłuższego
# znajdującego się w niej ciągu arytmetycznego o dodatniej różnicy, a długością najdłuższego ciągu arytmetycznego
# o ujemnej różnicy, przy założeniu, że kolejnymi wyrazami ciągu są elementy tablicy o kolejnych indeksach.

def longest_pos_and_neg_arithmetic_subsequence(t :list)->tuple[int,int]:
    if len(t) < 2 or (len(t)==2 and t[0]==t[1]):
        return (0,0)
    best_neg_length, best_pos_length = 0,0
    r = t[1]-t[0]
    counter = 2
    for i in range(2,len(t)):
        if t[i]-t[i-1]==0:
            continue

        if t[i]-t[i-1]==r:
            counter+=1
        else:
            if r>0:
                best_pos_length = max(best_pos_length, counter)
            elif r<0:
                best_neg_length = max(best_neg_length, counter)
            counter = 2
            r = t[i]-t[i-1]
    if r>0:
        best_pos_length = max(best_pos_length, counter)
    elif r<0:
        best_neg_length = max(best_neg_length, counter)
    return (best_neg_length, best_pos_length)

assert longest_pos_and_neg_arithmetic_subsequence([1,2,3,4,3,2,1,0]) == (5,4)
assert longest_pos_and_neg_arithmetic_subsequence([1,2,3,4,5,6,7,8]) == (0,8)
assert longest_pos_and_neg_arithmetic_subsequence([2,2,2,2,2,2,2]) == (0,0)
assert longest_pos_and_neg_arithmetic_subsequence([2,2,2,2,2,1]) == (2, 0)
assert longest_pos_and_neg_arithmetic_subsequence([3,2,2,2,2,3]) == (2,2)
assert longest_pos_and_neg_arithmetic_subsequence([1,2,3,1,2,3,4,5,5,5,5,3,2,-1,-2]) == (2, 5) 
assert longest_pos_and_neg_arithmetic_subsequence([1,2,3,1,2,3,4,5,5,5,5,3,1,-1,-3]) == (5, 5) 
assert longest_pos_and_neg_arithmetic_subsequence([1,2]) == (0,2)
print("OK!")
