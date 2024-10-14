# Zadanie 33. Proszę napisać program wczytujący liczbę naturalną i odpowiadający na pytanie, 
# czy jej cyfry stanowią ciąg geometryczny.
def are_digits_geo_progression(n :int)->bool:
    if n < 10 or n%10==0 or n%100<10:
        return False

    q = n%100//10/(n%10)
    n//=10
    while n > 10:
        if n%10 == 0 or n%100==0 or  n%100//10/(n%10) != q:
            return False
        n//=10
    return True

n = int(input("Podaj liczbę: "))
print("Czy cyfry stanowią ciąg geometryczny:", are_digits_geo_progression(n))

assert are_digits_geo_progression(0) == False
assert are_digits_geo_progression(1248) == True
assert are_digits_geo_progression(8421) == True 
assert are_digits_geo_progression(111111) == True
assert are_digits_geo_progression(931) == True
assert are_digits_geo_progression(0) == False
