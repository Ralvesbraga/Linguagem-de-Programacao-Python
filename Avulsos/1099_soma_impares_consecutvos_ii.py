n = int(input())
for i in range(n):
    x, y = input().split()
    x = int(x)
    y = int(y)
    soma = 0
    if x > y:
        for j in range(y + 1, x):
            if j % 2 == 1:
                soma = soma + j
    if y > x:
        for j in range(x + 1, y):
            if j % 2 == 1:
                soma = soma + j
    print(soma)
