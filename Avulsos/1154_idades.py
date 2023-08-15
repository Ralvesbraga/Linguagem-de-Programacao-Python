soma = 0
cont = 0
while True:
    x = int(input())
    if x < 0:
        print(f'{soma/cont :.2f}')
        break
    soma = soma + x
    cont += 1
