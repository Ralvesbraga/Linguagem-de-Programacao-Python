l, c = input().split()
l = int(l)
c = int(c)
matriz = []
for i in range(l):
    copia = input().split()
    linha = []
    for j in range(c):
        linha.append(int(copia[j]))
    matriz.append(linha)
somacoluna = [0] * c
somalinha = []
for i in range(l):
    soma = 0
    for j in range(c):
        soma = soma + matriz[i][j]
        somacoluna[j] = somacoluna[j] + matriz[i][j]
    somalinha.append(soma)
maiorcoleta = 0
for i in range(c):
    if somacoluna[i] > maiorcoleta:
        maiorcoleta = somacoluna[i]
maiorcoleta2 = 0
for i in range(l):
    if somalinha[i] > maiorcoleta2:
        maiorcoleta2 = somalinha[i]
if maiorcoleta > maiorcoleta2:
    print(maiorcoleta)
else:
    print(maiorcoleta2)
