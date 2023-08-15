while True:
    try:
        n = int(input())
        meliantes = input().split()
        suspeito1 = 0
        suspeito2 = 0
        indice = 0
        copia = []
        if n == 0:
            break
        for i in range(n):
            copia.append(int(meliantes[i]))
            if copia[i] > suspeito1:
                suspeito1 = copia[i]
                indice = i
        calma = copia.pop(indice)
        for i in range(n - 1):
            if copia[i] > suspeito2:
                suspeito2 = copia[i]
        copia.append(calma)
        for i in range(n):
            if str(suspeito2) == meliantes[i]:
                print(i + 1)
    except EOFError:
        break
