# Zadanie 63. Proszę napisać program obliczający i wypisujący stałą e z rozwinięcia w szereg 
# e = 1/0! + 1/1! + 1/2! + 1/3! + ... z dokładnością N cyfr dziesiętnych (N jest rzędu 1000).

# Brak wymaganej dokładności, przypuszczam, że wymagane jest przechowywanie każdej z cyfr 
# w osobnej komórce tablicy. Jak to skutecznie wdrożyć? Jeszcze nie wiem 
# EDIT: Miałem rację
def calculate_e(n :int)->float:
    
    e = t = 1.0
    for i in range(1, n+1):
        e+= 1.0/t
        t *= i
    return e

def add_lists(e:list, w:list)->list:
    carry = 0
    for i in range(len(e)-1, -1, -1):
        sum = e[i] + w[i] + carry
        carry, e[i] = divmod(sum, 10)

    return e 

def divide_lists(w: list[int], n :int)->tuple[list[int], bool]:
    continue_division = False
    carry = 0
    for i in range(len(w)):
        sum = 10*carry + w[i]
        w[i] = sum//n
        if w[i]>0:
            continue_division = True
        carry = sum%n
    
    return w, continue_division


# e - liczba e | w - kolejny wyraz 1/N!
def oblicz_e_garek(d :int)->str:
    e = [0 for _ in range(d)]
    w = [0 for _ in range(d)]
    e[0],w[0]=1,1

    n = 2
    continue_division = True
    while continue_division:
        e = add_lists(e,w)
        w, continue_division = divide_lists(w, n)
        n+=1
    return "2."+ "".join([str(x) for x in e[1:]])

n = int(input("Podaj dokładność N: "))
print(oblicz_e_garek(n))

""" 
___ Garek Content ___ 

calculate_e lepiej robić dzieląc wyraz w, niż mnożyć wyraz t i dzielić go przez 1 

Ten program trzeba będzie porządnie rozrysować na kartce . _. 



Porównaj linijki kodu calculate_e() oraz oblicz_e_garek(). Pełnią one podobne funkcje

"""
