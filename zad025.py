# Zadanie 25. Proszę napisać program wczytujący liczbę naturalną i odpowiadający na pytanie, czy liczba
# ta jest iloczynem dowolnych dwóch wyrazów ciągu Fibonacciego.

def is_fibonacci_product(n :int)->bool:
    a,b=1,1
    occur = set([1])
    while a <= n:
        if n/a in occur:
            return True
        occur.add(a)
        c = a+b
        a = b
        b = c 
    return False        

n = int(input("Podaj N: "))
print("Czy iloczyn Fibonacciego:", is_fibonacci_product(n))
