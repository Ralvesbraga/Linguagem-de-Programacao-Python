vlr = float(input())
v1 = [100.00, 50.00, 20.00, 10.00, 5.00, 2.00]
v2 = [1.00, 0.50, 0.25, 0.10, 0.05, 0.01]
inteiro = int(vlr)
moeda = (vlr - inteiro)
nmoedas = 0
print('NOTAS:')
for i in v1:
    nota = vlr // i
    vlr = vlr - (nota * i)
    nota = int(nota)
    print('{} nota(s) de R$ {:.2f}'.format(nota, i))
    vlr = round(vlr, 2)
print('MOEDAS:')
for j in v2:
    if j > 0.01:
        nmoedas = vlr // j
        vlr = vlr - (nmoedas * j)
        nmoedas = int(nmoedas)
        print('{} moeda(s) de R$ {:.2f}'.format(nmoedas, j))
    else:
        vlr = round(vlr, 2)
        nmoedas = vlr / j
        vlr = vlr - (nmoedas * j)
        nmoedas = int(nmoedas)
        print('{} moeda(s) de R$ {}'.format(nmoedas, j))
