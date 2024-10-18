# Zadanie 67. Dana jest N-elementowa tablica T zawierająca liczby naturalne. 
# W tablicy możemy przeskoczyć z pola o indeksie k o n pól w prawo jeżeli wartość n jest czynnikiem pierwszym liczby T[k]. 
# Napisz funkcję sprawdzającą, czy jest możliwe przejście z pierwszego pola tablicy na ostatnie pole.

# tldr; zaznaczamy na drugiej tablicy pola, do których można doskoczyć, z pola, na którym obecnie stoimy

def check_possile_fields(t :list, available : list, i :int)->None:
    num = t[i]

    k = 2
    while num > 1 and i+k<len(t): 
        if num%k == 0:
            available[i+k]=True
            while num%k==0:
                num//=k
        k+=1
    return 


def can_reach_end(t:list)->bool:
    available = [False]*len(t)
    available[0]=True
    for i in range(len(t)-1):
        check_possile_fields(t, available, i)
    print(available)

    return available[-1]

# ___Wywołanie___:
t = [6,17,18, 125,15,2,1,0]
print(t)
print("Czy doskoczy na ostatnie pole:", can_reach_end(t))


# ___Testy___:
assert can_reach_end([0]) == True
assert can_reach_end([456,0,123]) == True
assert can_reach_end([1,1,1,1,1,1,1]) == False

