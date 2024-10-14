# Zadanie 13. Liczba doskonała to liczba równa sumie swoich podzielników właściwych (mniejszych od
# jej samej), na przykład 6 = 1 + 2 + 3. Proszę napisać program wyszukujący liczby doskonałe mniejsze od miliona.

def sum_of_divisors(n : int)->int:
    if n == 1:
        return 1
    i = 2
    sum = 1
    while i*i < n:
        if n%i==0:
            sum += i + n//i
        i+=1
    if i*i == n:
        sum += i
    return sum

def perfect_numbers_generator(n :int)->None:
    
    for i in range(2, n+1): 
        if sum_of_divisors(i) == i: print(i)

n = int(input("Podaj granicę: "))
print("Liczby doskonale:")
perfect_numbers_generator(n)
