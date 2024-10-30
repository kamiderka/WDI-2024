# Zadanie 80. Dana jest tablica T[N] wypełniona niepowtarzającymi się liczbami naturalnymi. Proszę
# napisać funkcję trojki(T) która zlicza wszystkie trójki liczb, które spełniają następujące warunki:
# (1) największym wspólnym dzielnikiem trzech liczb jest liczba 1,
# (2) pomiędzy dwoma kolejnymi elementami trójki może być co najwyżej jedna przerwa.
# Funkcja powinna zwrócić liczbę znalezionych trójek.

def NWD(a: int, b :int)->int:
    while b != 0:
        temp = b
        b = a % b
        a = temp
    return a


def trojki(t :list)->int:
    if len(t)<3:
        return 0
    result = 0
    nums = [0 for _ in range(len(t)+2) ]
    for i in range(0, len(t)):
        nums[i]=t[i]
    for i in range(len(nums)-4):
        for x in (1,2):
            for y in (1,2):
                a = nums[i]
                b = nums[i+x]
                c = nums[i+x+y]
                if NWD(a,b) == 1 and NWD(a,c) == 1  and NWD(b,c) == 1:
                    result += 1
    return result

assert trojki([2,4,6,7,8,10,12]) == 0 
assert trojki([2,3,4,6,7,8,10]) == 1 # trójka (3,4,7)
assert trojki([2,4,3,6,5])  == 2 # trójki (2,3,5),(4,3,5)
assert trojki([2,3,4,5,6,8,7]) == 5 # trójek (2,3,5),(3,4,5),(3,5,8),(5,6,7),(5,8,7)
assert trojki([2,3,5]) == 1
print("OK!")
