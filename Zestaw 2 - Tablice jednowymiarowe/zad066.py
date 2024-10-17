# Zadanie 66. Napisać program wypełniający N-elementową tablicę T liczbami pseudolosowymi z zakresu
# 1-1000 i sprawdzający czy istnieje element tablicy zawierający wyłącznie cyfry nieparzyste.
from random import randint

def has_odd_digits_only(num :int)->bool:
    while num>0:
        if num%2==0:
            return False
        num//=10
    return True

# Przeczucie mówi mi, że to zadanie na bit-shifty... Trzeba kiedyś się za nie wziąć.
def has_odd_digits_only_number_in_nums(nums :list)->bool:
    for num in nums:
        if has_odd_digits_only(num):
            return True

    return False

n = int(input("Podaj N (długość listy): "))
arr = [randint(1,1000) for _ in range(n)]
print(arr)
print("Czy istnieje liczba złożona tylko z cyfr nieparzystych: ", has_odd_digits_only_number_in_nums(arr))
