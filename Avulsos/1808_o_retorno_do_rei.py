num = input()
soma = 0
cont = 0
for i in num:
    if i == '0':
        soma += 9
    else:
        soma += int(i)
        cont += 1
print(f'{soma/cont:.2f}')
