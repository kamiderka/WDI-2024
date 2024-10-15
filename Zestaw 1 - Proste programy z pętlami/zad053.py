# Zadanie 53. Liczba dwu-trzy-piątkowa w rozkładzie na czynniki pierwsze nie posiada innych czynników
# niż 2, 3, 5. Jedynka też jest taką liczbą. Proszę napisać program, 
# który wylicza ile takich liczb znajduje się w przedziale od 1 do N włącznie.

#
def ile_235(n: int)->int:
    counter = 0
    i2 = 1
    while i2<=n:
        i3=i2
        while i3<=n:
            i5=i3
            while i5 <=n:
                counter+=1
                i5*=3
            i3*=3
        i2 *= 2

    return counter



def how_many_235_numbers(n :int)->int:
    pass

""" 
Garek content: 
i2  i3      i5      counter
1   1       1       0
    3       5       1
    9       25      2
    27 ///kolega dalej liczy 


Piękne rozwiązanie:

counter+=1
for(int i2=1; i2<=n; i2*=2)
for(int i3=i2; i3<=n; i3*=3)
for(int i5=i3; i5<=n; i5*=5) counter+=1

"""

n = int(input("Podaj N: "))
print("Liczb 2-3-5 do N:", how_many_235_numbers(n))
