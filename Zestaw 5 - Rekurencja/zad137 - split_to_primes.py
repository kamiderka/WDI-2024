""" ===============================
Zadanie 137. Dany jest ciąg zer i jedynek zapisany w tablicy T[N]. Proszę napisać funkcję, która odpowiada na pytanie czy jest możliwe pocięcie ciągu na kawałki z których każdy reprezentuje liczbę pierwszą.
Długość każdego z kawałków nie może przekraczać 30. Na przykład dla ciągu 111011 jest to możliwe, a dla
ciągu 110100 nie jest możliwe.
==============================="""

def is_prime(n: int)->bool:
    if n < 2: return False

    i = 2
    while i*i<=n:
        if n%i ==0:
            return False
        i+=1
    return True

def split_to_primes(T :list[int], i :int) -> bool:
    if i == -1: return True
    if T[i] == 0: return False

    k = 1
    num = 0
    for j in range(i, max(-1, i-31), -1):
        num += k*T[j]
        if is_prime(num):
            if split_to_primes(T, j-1):
                if i == len(T)-1 and j == 0: return False
                return True
        k*= 2
    return False

def zad137(T :list[int])->bool:
    i = len(T)-1
    return split_to_primes(T, i)

def test_zad137():
    # Test 1: Przyklad z zadania
    assert zad137([1, 1, 1, 0, 1, 1]) == True  # 111011, możliwe podzielenie na liczby pierwsze
    assert zad137([1, 1, 0, 1, 0, 0]) == False  # 110100, niemożliwe podzielenie

    # Test 2: Krótkie ciągi
    assert zad137([1, 0]) == False  # 10 -> 2 (pierwsza) - ale nie ma jak podzielić
    assert zad137([1, 1]) == False  # 11 -> 3 (pierwsza) - ale nie ma jak podzielić
    assert zad137([0, 0]) == False  # 00 -> 0 (nie pierwsza)

    # Test 3: Jednoelementowe ciągi
    assert zad137([1]) == False  # 1 - nie jest liczbą pierwszą
    assert zad137([0]) == False  # 0 - nie jest liczbą pierwszą

    # Test 4: Długi ciąg, który można podzielić
    assert zad137([1, 1, 0, 1, 1, 1, 0, 1]) == True  # 11101110, możliwe podzielenie

    # Test 5: Ciąg, który nie ma podziału na liczby pierwsze
    assert zad137([1, 1, 1, 0, 0, 0, 1, 0]) == False  # 11100010, brak podziału na liczby pierwsze

    # Test 6: Losowe testy
    assert zad137([1, 1, 1, 1, 0, 0, 1]) == False
    assert zad137([1, 0, 0, 1, 0, 1, 0]) == False

    print("Wszystkie testy przeszły pomyślnie!")

# Uruchomienie testów
test_zad137()
