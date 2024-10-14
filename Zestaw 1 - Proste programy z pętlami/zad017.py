# Zadanie 17. Proszę napisać program obliczający wartości cos(x) z rozwinięcia w szereg Maclaurina.

def calculate_maclaurin(x :float, eps=10e-5)->float:

   prev = 0
   a = 1
   b = 1
   c = 1

   result = (a/b)*c
   n = 1
   while abs(result - prev) > eps:
       a = -a
       b *= 2*n*(2*n-1)
       c *= x**2
       prev = result
       result += (a/b)*c 
       n+=1
   return '{:f}'.format(result)

# Better solution tbh
# def calculate_maclaurin(x: float, eps=1e-10) -> float:
#     prev = 0
#     term = 1  # Pierwszy wyraz szeregu (x^0 / 0!)
#     result = term
#     n = 1
#
#     while abs(result - prev) > eps:
#         prev = result
#         term *= -x**2 / (2 * n * (2 * n - 1))  # Obliczamy następny wyraz
#         result += term
#         n += 1
#
#     return result


n = float(input("Podaj x: "))
print("cos(x) =", calculate_maclaurin(n))
