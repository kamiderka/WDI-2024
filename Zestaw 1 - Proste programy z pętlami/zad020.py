# Zadanie 20. Dla ciągu z poprzedniego zadania proszę znaleźć najmniejszy wyraz początkowy N, dla
# którego ciąg osiąga wartość 1 dokładnie po N krokach.


def steps_until_1(a :float)->int:
    n=0
    while a != 1:
        if a%2:
            a = 3*a+1
        else:
            a /= 2 
        n+=1
    return n

def beg_to_reach_N_steps(n :int)->int:
    if n < 2: 
        return float('nan')
    i=2
    while steps_until_1(i)!=n:
        i+=1
    return i

n = int(input("Podaj N: "))
print("Wyraz początkowy:", beg_to_reach_N_steps(n))
