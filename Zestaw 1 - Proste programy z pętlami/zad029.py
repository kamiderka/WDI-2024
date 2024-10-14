# Zadanie 29. Proszę napisać program wczytujący liczbę naturalną i odpowiadający na pytanie, czy liczba
# ta jest wielokrotnością dowolnego wyrazu ciągu danego wzorem A(n) = n∗ n + n+1.

def sequence_a(n :int)->int:
    return (n+1)*n + 1

def is_number_multiple_of_sequence(target :int)->bool:
    n = 2
    a = 3  
    while a <= target: 
        if target%a==0:
            return True
        n+=1
        a = sequence_a(n)
    
    return False

n = int(input("Podaj liczbę: "))
print("Czy wielokrotność A(n):", is_number_multiple_of_sequence(n))
