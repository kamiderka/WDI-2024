# Zadanie 12. Proszę napisać program wypisujący rozkład liczby na czynniki pierwsze.

def zad12(n :int)->None:
    i=2
    while n > 1:
        while n%i==0:
            print(i)
            n//=i
        i+=1
n = int(input("Podaj liczbę: "))
print("Czynniki pierwsze: ")
zad12(n)
