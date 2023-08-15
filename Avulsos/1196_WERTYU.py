while True:
    try:
        teclado_ruim = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '=', 'W', 'E', 'R', 'T', 'Y', 'U', 'I',
                        'O', 'P', '[', ']', '\\', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', ';', "'", 'X', 'C', 'V', 'B',
                        'N', 'M', ',', '.', '/']
        teclado_baum = ['`', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', 'Q', 'W', 'E', 'R', 'T', 'Y', 'U',
                        'I', 'O', 'P', '[', ']', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', ';', "Z", 'X', 'C', 'V',
                        'B', 'N', 'M', ',', '.']
        letras = input().split()
        indice = 0
        frase = ''
        for i in range(len(letras)):
            for j in range(len(letras[i])):
                letra = letras[i][j]
                indice = teclado_ruim.index(letra)
                frase += teclado_baum[indice]
            if i != len(letras) - 1:
                frase += ' '
        print('\n', frase)
    except EOFError:
        break
