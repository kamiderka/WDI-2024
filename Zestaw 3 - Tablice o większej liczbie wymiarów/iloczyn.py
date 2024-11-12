"""
    Znajdź wszystkie pary, których iloczyn wynosi p. 
    Follow-up: Dasz radę znaleźć n-ki? (para: n=2, trójka: n=3)
"""

from collections import defaultdict


def iloczyn(t :list[list[int]], p :int):
    pairs = 0 
    occur = defaultdict(int)
    for y in range(0,len(t)):
        for x in range(0, len(t)):
            x = t[y][x]
            if p%x == 0:
                if occur[p//x] > 0 :
                    pairs += occur[p//x]
                occur[x]+=1
    return pairs

print(
    iloczyn([
        [1,2,3,4],
        [1,2,3,4],
        [1,2,3,4],
        [1,2,3,4]]
    , 16)
)
