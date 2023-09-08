while True:
    try:
        contMa, contMi, contD = 0, 0, 0
        senha = input()
        if 6 <= len(senha) <= 32:
            if not senha.isalnum():
                print('Senha invalida.')
            else:
                for i in senha:
                    if i.isupper():
                        contMa = 1
                    elif i.islower():
                        contMi = 1
                    elif i.isdigit():
                        contD = 1
                if contMi == contMa == contD == 1:
                    print('Senha valida.')
                else:
                    print('Senha invalida.')
        else:
            print('Senha invalida.')
    except EOFError:
        break
