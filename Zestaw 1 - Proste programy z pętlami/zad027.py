# Zadanie 27. Proszę napisać program wczytujący liczbę naturalną i odpowiadający na pytanie, czy liczba
# naturalna jest palindromem, a następnie czy jest palindromem w systemie dwójkowym.

def is_dec_palindrome(n :int)->bool:
    org = n
    rev = 0
    while n > 0:
        rev = rev*10 + n%10
        n//=10
    return rev == org

# Bardziej garkowe rozwiązanie: https://www.geeksforgeeks.org/check-binary-representation-number-palindrome/
def is_bin_palindrome(n :int)->bool:
    result = ""
    while n>0:
        result += str(n%2)
        n//=2
    return result == result[::-1]

def is_bin_and_dec_palindrome(n:int)->bool:
    return is_dec_palindrome(n) and is_bin_palindrome(n)

n = int(input("Podaj liczbę: "))
print("Is bin and dec palindrome:", is_bin_and_dec_palindrome(n))
