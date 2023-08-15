let = input()
palavras = input().split()
cont = 0
for i in range(len(palavras)):
    if let in palavras[i]:
        cont += 1
porcentagem = (cont/len(palavras) * 100)
print(f'{porcentagem:.1f}')
