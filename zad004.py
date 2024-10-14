# Zadanie 4. Proszę napisać program sprawdzający czy istnieje spójny podciąg ciągu Fibonacciego o zadanej sumie.

def zad4(target :int)->bool:
    
    a,b = 1,1
    fib = []
    while a <= target:
        fib.append(a)
        c = a + b 
        a = b 
        b = c

    print(fib)

    start = 0
    curr_sum = 0 
    for end in range(len(fib)):
        print(start, end, curr_sum)
        if curr_sum == target:
            return True

        curr_sum += fib[end]

        while target < curr_sum and start <= end:
            curr_sum -= fib[start]
            start += 1 

    return curr_sum == target   

n = int(input("Podaj sumę: "))
print(zad4(n))
