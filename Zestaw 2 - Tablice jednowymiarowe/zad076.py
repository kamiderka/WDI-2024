# Zadanie 76. Dane są dwie N-elementowe tablice t1 i t2 zawierające liczby naturalne. Z wartości w obu tablicach możemy tworzyć sumy. „Poprawna” suma to taka, która zawiera co najmniej jeden element
# (z tablicy t1 lub t2) o każdym indeksie. Na przykład dla tablic: t1 = [1,3,2,4] i t2 = [9,7,4,8] poprawnymi
# sumami są na przykład 1+3+2+4, 9+7+4+8, 1+7+3+8, 1+9+7+2+4+8. Proszę napisać funkcje generującą
# i wypisująca wszystkie poprawne sumy, które są liczbami pierwszymi. Do funkcji należy przekazać dwie
# tablice, funkcja powinna zwrócić liczbę znalezionych i wypisanych sum.

def is_prime(n :int)->bool:
    if n < 2:
        return False
    
    i=2
    while i*i<=n:
        if n%i==0:
            return False
        i+=1
    return True

def get_number_from_mask(t1 :list, t2 :list, m :int)->int:
    result = 0
    for i in range(len(t1)):
        if m%3 > 0:
            result += t2[i]
        if (m%3)%2 == 0:
            result += t1[i]
        m//=3
    print(result, end=", ")
    return result

def get_prime_sums(t1 :list, t2 :list)->tuple[int,int]:
    assert len(t1)==len(t2)
    counter = 0
    for m in range(0, 3**(len(t1))):
        num = get_number_from_mask(t1,t2,m)
        if is_prime(num):
            counter += 1
        print()
    return 3**(len(t1)),counter

print(get_prime_sums([1,2,3,4],[5,6,7,8]))

# __Testy__:
t1 = [1, 4, 52, 3, 5, 2, 35] 
t2 = [33, 0, 93, 5, 12, 2, 5]
expected = 410
assert get_prime_sums(t1, t2)[1] == expected # 1

t1 = [1, 3, 2, 4]
t2 = [9, 7, 4, 8]
expected = 17
assert get_prime_sums(t1, t2)[1] == expected #2 

t1 = [1,2]
t2 = [9,4]
expected = 5
assert get_prime_sums(t1, t2)[1] == expected #3

t1 = [1,4]
t2 = [3,5]
expected = 3
assert get_prime_sums(t1, t2)[1] == expected #4 

t1=[1,0]
t2=[0,6]
expected = 4
assert get_prime_sums(t1, t2)[1] == expected #5

print("OK!")

