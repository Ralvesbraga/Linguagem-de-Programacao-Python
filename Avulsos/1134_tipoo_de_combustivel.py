clientes = [0] * 3
while True:
    n = int(input())
    if n == 1:
        clientes[0] += 1
    elif n == 2:
        clientes[1] += 1
    elif n == 3:
        clientes[2] += 1
    if n == 4:
        print('MUITO OBRIGADO')
        print(f'Alcool: {clientes[0]}')
        print(f'Gasolina: {clientes[1]}')
        print(f'Diesel: {clientes[2]}')
        break
