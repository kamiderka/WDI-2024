# Zadanie 61. Napisać funkcje sprawdzającą czy dwie liczby naturalne są one 
# zbudowane z takich samych cyfr, np. 123 i 321, 1255 i 5125, 11000 i 10001.

def are_same_digits(a:int,b:int)->bool:
    occur = [0]*10
    while a>0:
        occur[a%10]+=1
        a//=10

    while b>0:
        occur[b%10]-=1
        b//=10
    
    for el in occur:
        if el != 0:
            return False
    return True

# Input
a = int(input("Podaj liczbę a: "))
b = int(input("Podaj liczbę b: "))
print("Czy te same cyfry:",are_same_digits(a,b))

# Testy
assert are_same_digits(123,321) == True
assert are_same_digits(1255,5125) == True
assert are_same_digits(11000,10001) == True
assert are_same_digits(1255,51255) == False
