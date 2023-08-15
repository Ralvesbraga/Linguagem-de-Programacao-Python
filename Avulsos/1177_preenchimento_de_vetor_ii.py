n = int(input())
vet = [0] * 1000
cont = 0
for i in range(1000):
    print(f'N[{i}] = {cont}')
    if cont == n - 1:
        cont = 0
    else:
        cont += 1
