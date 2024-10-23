# Zadanie 64. Napisać program, który wczytuje wprowadzany z klawiatury ciąg liczb naturalnych zakończonych 
# zerem stanowiącym wyłącznie znacznik końca danych. Program powinien wypisać 10 co do wielkości
# wartość, jaka wystąpiła w ciągu. Można założyć, że w ciągu znajduje się wystarczająca liczba elementów.

# Zadanie inspirowane chyba insertion sortem
def kth_highest_element(k:int)->int:
    assert k >0
    top_table = [0]*k
    n = int(input("> "))
    while n != 0:
        if n>top_table[0] and n not in top_table: # usuwając drugi warunek sprawdzamy elementy, nie wartości
            i=1
            while i < k and n>top_table[i]:
                top_table[i-1] = top_table[i]
                i+=1
            top_table[i-1] = n
        print(top_table)
        n = int(input("> "))

    return top_table[0]

k = int(input("Podaj k: "))
print(str(k)+"-ta największa liczba:",kth_highest_element(k))

"""
___Garek Content___
Co mierzymy? 10 największych WARTOŚCI (nie elementy).

"""
