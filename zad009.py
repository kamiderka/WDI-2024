# Zadanie 9. Proszę napisać program wczytujący liczbę naturalną i odpowiadający na pytanie, czy liczba ta jest iloczynem dowolnych dwóch kolejnych wyrazów ciągu Fibonacciego.

def zad9(target :int)->bool:
    a, b = 1,1
    while a*b < target:
        c = a+b
        a = b
        b = c 
    return a*b == target

n = int(input("Podaj liczbę: "))
print("Czy iloczyn Fibonacciego:", zad9(n))
