# Zadanie 26. Proszę napisać program wczytujący trzy liczby naturalne a, b, n i wypisujący rozwinięcie
# dziesiętne ułamka a/b z dokładnością do n miejsc po kropce dziesiętnej. (n jest rzędu 100)

def precise_division(a :int, b :int, n :int)->str:
    result = ""
    result += str(a//b) + "."
    for _ in range(n):
        a*= 10 
        result += str(a//b)
        a = (10*a)%b
    return result

""" 
____Garek Content_____
for _ in range(n):

"""

a = int(input("Podaj a: "))
b = int(input("Podaj b: "))
n = int(input("Podaj n: "))
print("Wynik dzielenia:", precise_division(a,b,n))

assert precise_division(123124, 53654635, 200) == "0.00229475049080102772109063830179815779195963219207436598907065531244411596500470089862693129866599595729241285491924416222382278809649902566665489384095148536561659584488833070991909645830225105435905"
