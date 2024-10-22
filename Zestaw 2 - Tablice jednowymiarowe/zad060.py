# Zadanie 60. Napisać funkcję zamieniającą i wypisującą liczbę naturalną na system o podstawie 2-16.
from math import log, ceil

def convert_digit(a:int)->str:
    if a < 10:
        return str(a)
    return chr(ord('A') + a - 10 )

def convert_to_base(n: int, base :int)->str:
    bits = ceil(log(n, base))
    converted_number = [None]*bits 
    
    i = len(converted_number)-1
    while n>0:
        converted_number[i]=convert_digit(n%base)
        n//=base
        i-=1

    return "".join(converted_number)


n = int(input("Podaj numer: "))
base = int(input("Podaj bazę: "))

print(convert_to_base(n,base))

"""
___ Garek Content ___
Garek nie lubi linijki 
    `converted_number = [None]*bits`
preferuje wyrażenie listowne. (Problem z referencjami or sth)

zamiast funkcji convert_digit string
` hex = "01234556789ABCDE"

"""
