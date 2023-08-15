while True:
    j, p = map(int, input().split())
    if j == p == 0:
        break
    matriz = []
    caso1 = 1
    caso2 = 1
    caso3 = 1
    caso4 = 1
    for i in range(j):
        problemas = list(map(int, input().split()))
        matriz.append(problemas)
    v1 = [0] * p
    for i in range(j):
        cont1 = 0
        for k in range(p):
            cont1 += matriz[i][k]
            v1[k] += matriz[i][k]
        if cont1 == p:
            caso1 = 0
        if cont1 == 0:
            caso4 = 0
        if j in v1:
            caso3 = 0
    if 0 in v1:
        caso2 = 0
    print(caso1 + caso2 + caso3 + caso4)
    