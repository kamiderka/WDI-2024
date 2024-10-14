# Zadanie 34. Proszę napisać program wczytujący liczbę naturalną i odpowiadający na pytanie, 
# czy liczba ta zawiera cyfrę równą liczbie swoich cyfr.

def contains_its_length_digit(n :int)->bool:
    occur = [False]*10
    i=0
    while n > 0 and i < 9:
        occur[n%10]=True
        n//=10
        i+=1
    return occur[i] and not n

n = int(input("Podaj liczbę: "))
print("Czy zawiera cyfrę długości:", contains_its_length_digit(n))

