# Zadanie 74. Dana jest duża tablica T. Proszę napisać funkcję, która zwraca informację czy w tablicy
# zachodzi następujący warunek: „wszystkie elementy, których indeks jest elementem ciągu Fibonacciego są
# liczbami złożonymi, a wśród pozostałych przynajmniej jedna jest liczbą pierwszą”

from random import randint

def is_prime(n :int) -> bool:
    if n < 2: 
        return False
    i=2
    while i*i<=n:
        if n%i == 0:
            return False
        i+=1
    return True

"""
1) Sprawdzamy czy przynajmniej jedna l.pierwsza do indeksu b
2) Sprawdzamy, czy b jest liczą złożoną
3) obliczany nowe b, przesuwamy początek przeszukiwania
4) Sprawdzamy, czy w ostatnim odcinku znajduje się liczba pierwsza
"""
def fibonacci_prime_filter(t :list)->bool:
    if len(t) == 1:
        return is_prime(t[0])

    a,b = 1, 1
    i,length = 0, len(t) 
    while b < length:
        found_prime = False
        while not found_prime and i < b:
            if is_prime(t[i]):
                found_prime = True
                break               
            print(t[i], found_prime)
            i+=1
           

        if (not found_prime and i != b)  or is_prime(t[b]):
            return False

        print("END:",i)
        
        c = a + b
        i = b+1
        a = b
        b = c

    if a == length: 
        return True

    for j in range(i, length):
        if is_prime(t[j]):
            return True

    return False

#    0 1 2 3  4 5  6  7  8   9 10 11
t = [2,4,4,8,17,16,18,39,16,10,12,12]
# print("Czy spełnia warunek:", fibonacci_prime_filter(t))

assert fibonacci_prime_filter([2,4,4,8,17,16,18,38,16,10,11,12]) == False
assert fibonacci_prime_filter([2,4,4,8,17,16,18,39,16,10,12,12]) == False
assert fibonacci_prime_filter([2,4,4,8,17,16,18,39,16,10,11,12]) == True
assert fibonacci_prime_filter([2]) == True
assert fibonacci_prime_filter([1]) == False
assert fibonacci_prime_filter([1,4]) == False
assert fibonacci_prime_filter([2,4]) == True

print("OK!")
