while True:
    try:
        entrada = input()
        entrada = list(entrada)
        entrada.reverse()
        soma = 0
        num = ''
        for i in range(len(entrada)):
            if entrada[i] == '=':
                soma += int(num)
                num = ''
            elif entrada[i] == '+':
                soma -= int(num)
                num = ''
            else:
                if i == len(entrada) - 1:
                    num += entrada[i]
                    soma -= int(num)
                else:
                    num += entrada[i]
        if soma == 0:
            print('True')
        else:
            print('False')
    except EOFError:
        break
