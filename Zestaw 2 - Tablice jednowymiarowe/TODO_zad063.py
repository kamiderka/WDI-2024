# Zadanie 63. Proszę napisać program obliczający i wypisujący stałą e z rozwinięcia w szereg 
# e = 1/0! + 1/1! + 1/2! + 1/3! + ... z dokładnością N cyfr dziesiętnych (N jest rzędu 1000).

# Brak wymaganej dokładności, przypuszczam, że wymagane jest przechowywanie każdej z cyfr 
# w osobnej komórce tablicy. Jak to skutecznie wdrożyć? Jeszcze nie wiem
def calculate_e(n :int)->float:
    
    e = t = 1.0
    for i in range(1, n+1):
        e+= 1.0/t
        print(t)
        t *= i
    return e

n = int(input("Podaj dokładność N: "))
print(calculate_e(n))
