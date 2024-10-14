# Zadanie 22. Proszę napisać program wyznaczający wartość liczby e korzystając z zależności: 
# e = 1/0! + 1/1! + 1/2! + 1/3! + ...

def calculate_e(eps=10e-20)->float:
    prev=0
    S=1
    n=1 
    factorial = 1
    while S - prev > eps:
        prev = S
        factorial /= n
        S += factorial
        n += 1

    return S
        
print("e =", calculate_e())
