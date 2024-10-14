# Zadanie 24. Pewne liczby pierwsze są palindromami i pozostają liczbami pierwszymi pomimo pozbawiania
# ich skrajnych cyfr. Na przykład: 71317 → 131 → 3. Proszę napisać program, który wypisuje wszystkie takie
# liczby mniejsze od N.

def is_prime(n :int)->bool:
    if n < 2:
        return False

    i=2
    while i*i<=n:
        if n%i == 0:
            return False
        i+=1
    return True

def is_palindrome(n : int)->(bool,int):
    rev = 0
    org = n
    i = 0
    while n>0:
        rev = rev*10 + n%10
        i+=1
        n//=10
    return rev==org, i

def is_prime_palindrome(n :int)->bool:
    is_palin, length = is_palindrome(n)
    if not is_palin or not is_prime(n):
        return False
    top = 10**(length-2)
    while n > 10:
        if not is_prime(n):
            return False
        n//=10
        n%=top
        top//=100
        
    
    return is_prime(n)

def find_prime_palindromes(n :int) -> None:
    
    for i in range(2,n+1):
        if is_prime_palindrome(i):
            print(i)

n = int(input("Podaj N: "))
print("Prime Palindromes: ")
find_prime_palindromes(n)
