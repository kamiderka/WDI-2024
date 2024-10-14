# Zadanie 31. Proszę napisać program wczytujący liczbę naturalną i odpowiadający na pytanie, czy liczba
# ta jest wielokrotnością dowolnego wyrazu ciągu danego wzorem An = 3 ∗ An−1 + 1, a pierwszy wyraz jest równy 2. 

def is_number_multiple_of_sequence(target :int)->bool:
    a = 7
    while a <= target:
        if target % a == 0:
            return True
        a = 3*a+1

    return False

n = int(input("Podaj liczbę: "))
print("Czy wielokrotność A(n):", is_number_multiple_of_sequence(n))

