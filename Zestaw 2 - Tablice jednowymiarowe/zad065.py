# Zadanie 65. Napisać program wypełniający N-elementową tablicę T liczbami naturalnymi 1-1000 
# i sprawdzający czy każdy element tablicy zawiera co najmniej jedną cyfrę nieparzystą.

from random import randint

# Jeśli co najmniej jedna liczba nieparzysta -> False 
def has_only_even_digits(num: int)->bool:
    while num>0:
        if num%2:
            return False
        num //=10
    return True

def is_min_one_odd_digit_in_nums(nums :list)->bool:
    for num in nums:
        if has_only_even_digits(num):
            return False

    return True

n = int(input("Podaj N (długość listy): "))
arr = [randint(1,1000) for _ in range(n)]
print(arr)
print("Czy każda liczba ma co najmniej jedną cyfrę nieparzysta: ", is_min_one_odd_digit_in_nums(arr))
