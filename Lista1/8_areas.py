a, b, c = input().split(' ')
a = float(a)
b = float(b)
c = float(c)
pi = 3.14159
tri = (a * c)/2
cir = pi * (c * c)
tra = ((a + b) * c)/2
qua = b * b
ret = a * b
print('TRIANGULO: {:.3f}'.format(tri))
print('CIRCULO: {:.3f}'.format(cir))
print('TRAPEZIO: {:.3f}'.format(tra))
print('QUADRADO: {:.3f}'.format(qua))
print('RETANGULO: {:.3f}'.format(ret))
