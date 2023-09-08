while True:
    try:
        frase = input().split()
        frase.append('1')
        a = len(frase)
        cont = 0
        compara = ''
        quant = 0
        for i in range(a):
            for j in range(len(frase[i])):
                if cont == 0:
                    compara = frase[i][j].lower()
                    cont += 1
                    break
                elif frase[i][j].lower() == compara:
                    cont += 1
                    if i == len(frase) - 1:
                        if cont > 1:
                            quant += 1
                    break
                else:
                    if cont > 1:
                        quant += 1
                    compara = frase[i][j].lower()
                    cont = 1
                    break
        print(quant)
    except EOFError:
        break
