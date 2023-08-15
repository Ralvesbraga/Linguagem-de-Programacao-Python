a, b, c = input().split()
a = float(a)
b = float(b)
c = float(c)
aux = 0
if a < b > c:
    aux = a
    a = b
    b = aux
elif a < c > b:
    aux = a
    a = c
    c = aux
if a >= b + c:
    print('NAO FORMA TRIANGULO')
else:
    if a**2 == (b**2) + (c**2):
        print('TRIANGULO RETANGULO')
    elif a**2 > (b**2) + (c**2):
        print('TRIANGULO OBTUSANGULO')
    elif a**2 < (b**2) + (c**2):
        print('TRIANGULO ACUTANGULO')
if a == b and b == c:
    print('TRIANGULO EQUILATERO')
elif a == b or b == c or a == c:
    print('TRIANGULO ISOSCELES')
