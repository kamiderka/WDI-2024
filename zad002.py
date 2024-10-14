# Zadanie 2. Proszę napisać program wypisujący elementy ciągu Fibonacciego mniejsze od miliona.

def fib_to_n(N :int, prt=False)->None:
    a,b = 1,1
    while a<N:
        if prt:
            print(a)
        c = a + b
        a = b
        b = c


N = 1e6
fib_to_n(N)
