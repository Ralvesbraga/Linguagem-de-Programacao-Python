n = int(input())
for i in range(n):
    n1, n2 = input().split()
    tamanho = len(n2)
    if n1[len(n1) - tamanho:] == n2:
        print('encaixa')
    else:
        print('nao encaixa')
