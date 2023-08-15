n = int(input())
for i in range(n):
    nsalunos = []
    distnum = []
    alunos, num = input().split()
    copia = input().split()
    num = int(num)
    for j in range(int(alunos)):
        nsalunos.append(int(copia[j]))
        if nsalunos[j] >= num:
            distnum.append(nsalunos[j] - num)
        elif nsalunos[j] < int(num):
            distnum.append(num - nsalunos[j])
    nganhador = distnum[0]
    indice = 0
    for j in range(int(alunos)):
        if nganhador > distnum[j]:
            nganhador = distnum[j]
            indice = j
    print(indice + 1)
