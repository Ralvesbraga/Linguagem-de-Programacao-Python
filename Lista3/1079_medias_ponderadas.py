n = int(input())
for i in range(1, n + 1):
    x, y, z = input().split()
    x = float(x)
    y = float(y)
    z = float(z)
    soma = (x * 2) + (y * 3) + (z * 5)
    print('{:.1f}'.format(soma/10))
