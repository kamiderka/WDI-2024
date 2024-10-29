# Zadanie 77. Dana jest N-elementowa tablica t jest wypełniona liczbami naturalnymi. Proszę napisać
# funkcję, która zwraca długość najdłuższego spójnego podciągu będącego palindromem złożonym wyłącznie
# z liczb nieparzystych. Do funkcji należy przekazać tablicę, funkcja powinna zwrócić długość znalezionego
# podciągu lub wartość 0 jeżeli taki podciąg nie istnieje.

def longest_odd_palindrome(t :list)->int:
    longest = 0
    for i in range(len(t)):
        if t[i]%2 == 1:
            for j in range(len(t)-1,i-1,-1):
                left,right=i,j
                while left<right and t[left]==t[right] and t[left]%2:
                    left += 1
                    right -= 1
                    if left >= right and t[left]%2:
                        longest = max(longest, j-i+1)
                        break
    return longest

t1 = [2,3,1,5,1,3,2,4,5,5,3,1,2,2]
expected = 5
assert longest_odd_palindrome(t1) == expected #1 

t1 = [2,3,1,2,1,3,2,4,5,5,3,1,2,2]
expected = 2
assert longest_odd_palindrome(t1) == expected #2 

t1 = [2,4,444,42,2,2,4,4,4,4,4,2,2]
expected = 0
assert longest_odd_palindrome(t1) == expected #3
print("OK!")
