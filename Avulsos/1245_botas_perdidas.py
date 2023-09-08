while True:
    try:
        n = int(input())
        par = 0
        botas = []
        for i in range(n):
            num, l = input().split()
            entrada = num + l
            if entrada[2] == 'D':
                if entrada[:2] + 'E' in botas:
                    par += 1
                    botas.remove(entrada[:2] + 'E')
                else:
                    botas.append(entrada)
            else:
                if entrada[:2] + 'D' in botas:
                    par += 1
                    botas.remove(entrada[:2] + 'D')
                else:
                    botas.append(entrada)
        print(par)
    except EOFError:
        break
