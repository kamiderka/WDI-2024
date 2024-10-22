# Zadanie 73. Napisać program wyznaczający na drodze eksperymentu prawdopodobieństwo tego, że w
# grupie N przypadkowo spotkanych osób, co najmniej dwie urodziły się tego samego dnia roku. 
# Wyznaczyć wartości prawdopodobieństwa dla N z zakresu 20-40.
from random import randint

def random_birthday()->int:
    return randint(1,365 + (not randint(0,3))*1)

def has_same_birthday(t :list)->bool:
    occur = set()
    for el in t:
        if el in occur:
            return True
        occur.add(el)
    return False

def init_birthday_array(n :int)->list:
    return [random_birthday() for _ in range(n)]

def conduct_bd_experiment(n:int, size=1_000_000)->float:
    result = 0
    for _ in range(size):
        t = init_birthday_array(n)
        result += int(has_same_birthday(t))
    return result/size

print(conduct_bd_experiment(40))
