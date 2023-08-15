n = int(input())
for i in range(1, n+1):
    soma = 0
    x = int(input())
    for j in range(1, x):
        if x % j == 0:
            soma = soma + j
    if soma == x:
        print('{} eh perfeito'.format(x))
    else:
        print('{} nao eh perfeito'.format(x))
