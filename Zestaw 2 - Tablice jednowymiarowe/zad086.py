"""
Zadanie 86. Dwie liczby naturalne są 4-zgodne, jeżeli po zapisaniu ich w systemie o podstawie 4, zbiory
cyfr występujące w liczbie są identyczne. Na przykład:
13 = 31(4) i 23 = 113(4)
18 = 102(4) i 33 = 201(4)
107 = 1223(4) i 57 = 321(4).
Dana jest tablica T[N] zawierająca N liczb naturalnych. Proszę napisać funkcję, która zwraca długość najdłuższego podciągu (niekoniecznie spójnego) złożonego z liczb 4-zgodnych.
"""

def bin2dec(t :list)->int:
    k = 1
    result = 0
    for i in range(0, len(t)):
        if t[i]:
            result += k
        k*=2
    return result

def type_of_comp(a :int)->int:
    bin = [False for _ in range(4)]
    while a > 0 and not all(bin):
        bin[a%4]=True
        a//=4
    return bin2dec(bin)

def most_4_compliant(t :list)->int:
    if len(t)<2:
        return 0
    types = [0 for _ in range(17)]
    for i in range(0, len(t)):
        types[type_of_comp(t[i])]+=1
    result = max(types)
    return 0 if result < 2 else result



# __Testy__:
for i in range(1, 500):
    t = list(range(i + 1))  # Tworzymy listę od 0 do i
    types = {}
    for num in t:
        comp_type = type_of_comp(num)
        if comp_type in types:
            types[comp_type] += 1
        else:
            types[comp_type] = 1

    # Liczymy maksymalną liczbę zgodnych typów, które mają przynajmniej 2 wystąpienia
    max_count = max((count for count in types.values() if count >= 2), default=0)

    assert most_4_compliant(t) == max_count, f"Błąd dla i={i}, oczekiwano {max_count}, otrzymano {most_4_compliant(t)}"

print("Wszystkie testy przeszły pomyślnie.")

