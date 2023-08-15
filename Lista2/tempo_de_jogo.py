inicio, fim = input().split()
inicio = int(inicio)
fim = int(fim)
if inicio > fim:
    tot = 24 - inicio + fim
elif inicio == fim:
    tot = 24
else:
    tot = fim - inicio
print('O JOGO DUROU {} HORA(S)'.format(tot))
