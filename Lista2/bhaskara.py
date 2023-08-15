from math import sqrt
a, b, c = input().split()
a = float(a)
b = float(b)
c = float(c)
delta = (b*b) - (4 * a * c)
if a == 0:
    print('Impossivel calcular')
elif delta >= 0:
    R1 = ((-b) + sqrt(delta))/(2 * a)
    R2 = ((-b) - sqrt(delta))/(2 * a)
    print('R1 = {:.5f}'.format(R1))
    print('R2 = {:.5f}'.format(R2))
else:
    print('Impossivel calcular')
