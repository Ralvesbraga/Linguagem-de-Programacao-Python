cod = []
nota = []
turma = 0
mcod = []
while True:
    mnota = 0
    mcod.clear()
    cod.clear()
    nota.clear()
    turma += 1
    n = int(input())
    if n == 0:
        break
    else:
        for i in range(n):
            x = input().split()
            cod.append(int(x[0]))
            nota.append(int(x[1]))
            x.clear()
        mnota = nota[0]
        for j in range(1, len(cod)):
            if nota[j] >= mnota:
                mnota = nota[j]
        for j in range(len(cod)):
            if nota[j] >= mnota:
                mcod.append(cod[j])
        print(f'Turma {turma}')
        for j in range(len(mcod)):
            if j == len(mcod) - 1:
                print(mcod[j], '\n')
            else:
                print(mcod[j], end=" ")
