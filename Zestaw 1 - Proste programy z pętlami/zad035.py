# Zadanie 35. Proszę napisać program wczytujący liczbę naturalną i odpowiadający na pytanie, czy liczba
# ta zakończona jest unikalną cyfrą.

def ends_with_unique_digit(n :int)->bool:
    assert n >=0
    
    last_digit = n%10
    n//=10
    while n>0:
        if n%10==last_digit:
            return False
        n//=10
    
    return True


n = int(input("Podaj liczbę: "))
print("Czy kończy się unikalną cyfrą:", ends_with_unique_digit(n))
