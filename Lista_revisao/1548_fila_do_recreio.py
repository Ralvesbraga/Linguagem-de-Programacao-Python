n = int(input())
for i in range(n):
    nalunos = int(input())
    fila = input().split()
    copia = []
    ind = 0
    cancel = 0
    resultado = 0
    for j in fila:
        copia.append(int(j))
    for j in range(nalunos):
        maior = copia[j]
        cancel = 0
        for k in range(j, nalunos):
            if maior < copia[k]:
                maior = copia[k]
                ind = k
                cancel = 1
        if cancel == 1:
            copia.insert(j, copia.pop(ind))
    for j in range(nalunos):
        if int(fila[j]) == copia[j]:
            resultado += 1
    print(resultado)
    