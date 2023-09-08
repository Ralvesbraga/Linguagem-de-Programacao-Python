while True:
    try:
        parametro = ''
        cont = 0
        frase = input().split()
        if frase[0] == '*':
            break
        for i in range(len(frase)):
            for j in range(len(frase[i])):
                if i == 0:
                    parametro = frase[0][0].lower()
                    cont += 1
                    break
                elif frase[i][0].lower() == parametro:
                    cont += 1
                    break
                else:
                    break
        if cont == len(frase):
            print('Y')
        else:
            print('N')
    except EOFError:
        break