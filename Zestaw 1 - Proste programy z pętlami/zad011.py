# Zadanie 11. Proszę napisać program wypisujący podzielniki liczby.

def zad11(n :int)->None:
    if n == 0:
        print("Każda liczba jest podzielnikiem")
    
    i,n=1,abs(n)
    while i*i < n:
        if n%i == 0: 
            print(i,n//i)
        i+=1
    if i*i==n: print(i)

n = int(input("Podaj liczbę: "))
print("Dzielniki:")
zad11(n)
