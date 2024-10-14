# Zadanie 14. Dwie różne liczby nazywamy zaprzyjaźnionymi gdy każda jest równa sumie podzielników
# właściwych drugiej liczby, na przykład 220 i 284. Proszę napisać program wyszukujący liczby zaprzyjaźnione mniejsze od miliona.

def divisor_sum(n:int)->int:
    if n == 1:
        return 1
    sum=1
    i=2
    while i*i < n:
        if n%i==0:
            sum+= i+n//i
            n//=i
        i+=1
    if i*i==n:
        sum+=1
    return sum

def amicable_number_generator(n:int)->None:
    pass
