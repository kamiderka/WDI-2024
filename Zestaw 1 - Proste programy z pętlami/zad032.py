# Zadanie 32. Proszę napisać program wczytujący liczbę naturalną i odpowiadający na pytanie, 
# czy jej cyfry stanowią ciąg rosnący.

def are_digits_increasing(n:int)->bool:
    if n < 12:
        return False
    prev = 10
    while n > 0:
        if n%10 >= prev:
            return False
        prev = n%10
        n//=10
    return True

n = int(input("Podaj liczbę: "))
print("Czy liczby stanowią ciąg rosnący:", are_digits_increasing(n))

assert are_digits_increasing(123456789) == True
assert are_digits_increasing(1) == False
assert are_digits_increasing(237) == True
assert are_digits_increasing(0) == False
assert are_digits_increasing(65432) == False
assert are_digits_increasing(123356) == False

