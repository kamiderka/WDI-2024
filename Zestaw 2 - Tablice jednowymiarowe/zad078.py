# Zadanie 78. Dana jest N-elementowa tablica t wypełniona liczbami naturalnymi. Proszę napisać funkcję,
# która zwraca długość najdłuższego, spójnego podciągu rosnącego dla którego suma jego elementów jest
# równa sumie indeksów tych elementów. Do funkcji należy przekazać tablicę, funkcja powinna zwrócić długość
# znalezionego podciągu lub wartość 0 jeżeli taki podciąg nie istnieje.

def longest_increasing_sequence(t :list)->int:
    longest = 0

    for i in range(0,len(t)-1):
        sum_tab = t[i]
        sum_ind = i
        for j in range(i+1, len(t)):
            if t[j]<=t[i]:
                break
            sum_tab += t[j]
            sum_ind += j
            if sum_ind == sum_tab:
                longest = max(longest, j-i+1)
    return longest

print(longest_increasing_sequence([1,2]))
# __Testy__:
assert longest_increasing_sequence([1,1,1,2,6]) == 3
assert longest_increasing_sequence([0,0]) == 0 
assert longest_increasing_sequence([0,1]) == 2 

print("OK!")

