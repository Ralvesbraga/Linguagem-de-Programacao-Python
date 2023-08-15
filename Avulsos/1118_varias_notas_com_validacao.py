while True:
    cont = 0
    cont += 1
    soma = 0
    if cont > 1:
        print('novo calculo (1-sim 2-nao)')
        segue = int(input())
        if segue == 2:
            break
    x = float(input())
    if cont > 1 > x > 2:
        print('novo calculo (1-sim 2-nao)')
        segue = int(input())
        if segue == 2:
            break
    if 0 <= x <= 10:
        soma = soma + x
        while True:
            y = float(input())
            if 0 <= y <= 10:
                soma = soma + y
                print(f'media = {soma / 2:.2f}')
            else:
                print('nota invalida')
    else:
        print('nota invalida')
