while True:
    try:
        frase = list(input())
        m = False
        letra = ''
        i = 0
        cont = 0
        while i < len(frase):
            if frase[i] != ' ' and cont == 0:
                letra = frase.pop(i)
                frase.insert(i, letra.upper())
                i += 1
                cont = 1
            else:
                if frase[i] == ' ':
                    i += 1
                else:
                    if m:
                        letra = frase.pop(i)
                        frase.insert(i, letra.upper())
                        m = False
                    else:
                        letra = frase.pop(i)
                        frase.insert(i, letra.lower())
                        m = True
                    i += 1
        print(*frase, sep='')
    except EOFError:
        break
