par = []
impar = []
for i in range(15):
    n = int(input())
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
    if len(par) == 5:
        for j in range(5):
            print(f'par[{j}] = {par[j]}')
            if j == 4:
                par = []
    elif len(impar) == 5:
        for j in range(5):
            print(f'impar[{j}] = {impar[j]}')
            if j == 4:
                impar = []
for j in range(len(impar)):
    print(f'impar[{j}] = {impar[j]}')
for j in range(len(par)):
    print(f'par[{j}] = {par[j]}')
