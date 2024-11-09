# Zadanie 48. Proszę napisać program wyznaczający najmniejszą liczbę pierwszą o sumie cyfr równej N,
# której cyfry są w porządku rosnącym


def sum_digits(n :int)->int:
    result=0
    prev = 10
    while n>0:
        curr = n%10
        if prev <= curr:
            return -1
        prev = curr
        result+=curr
        n//=10
    return result

def is_prime(n :int)->bool:
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n%2==0 or n%3==0:
        return False

    i = 3
    while i*i <= n:
        if n%i == 0:
            return False
        i+=2

        if n%i==0:
            return False
        i+=4
    return True


def ascending_digits_prime(n :int, border=10e50)->int:
    min_digits = n//9
    min_number = 10**min_digits

    for i in range(min_number, 123456789+1):
        if n%2!=0 or n%3!=0:
            if sum_digits(i) == n:
                if is_prime(i):
                    return i 
    return None
    
x = int(input("Podaj oczekiwaną sumę cyfr: "))
print("Upragniona liczba:",ascending_digits_prime(x))
