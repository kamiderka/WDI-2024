# Zadanie 19. Dany jest ciąg określony wzorem: An+1 = y(An mod 2) ∗ (3 ∗ An + 1) + (1 − An mod 2) ∗ An/2
# Startując z dowolnej liczby naturalnej > 1 ciąg ten osiąga wartość 1. Proszę napisać program, który znajdzie
# wyraz początkowy z przedziału 2-10000 dla którego wartość 1 jest osiągalna po największej liczbie kroków.

def steps_until_1(a :float)->int:
    n=0
    while a != 1:
        if a%2:
            a = 3*a+1
        else:
            a /= 2 
        n+=1
    return n

def max_steps_until_1(target :int)->int:
    result = -1
    for i in range(2, target+1):
        result = max(steps_until_1(i), result)
    return result

n = int(input("Podaj granicę przeszukiwania: "))
print("Max steps:", max_steps_until_1(n))
