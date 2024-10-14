# Zadanie 8. Proszę napisać program rozwiązujący równanie x**x = 2024 metodą bisekcji.

def zad8(target: int, eps=10e-10)->float:
    left, right = 0, 100
    
    while left < right:
        mid = (left+right)/2
        x = mid**mid-target
        if abs(x) <= eps:
            return mid
        elif x > 0:
            right = mid
        else:
            left = mid
    return -1

n = int(input("Podaj liczbę: "))
print("X =", zad8(n))
