cod1, nump, vl1 = input().split(' ')
cod2, nump2, vl2 = input().split(' ')
cod1 = int(cod1)
nump = int(nump)
vl1 = float(vl1)
cod2 = int(cod2)
nump2 = int(nump2)
vl2 = float(vl2)
total = (nump * vl1) + (nump2 * vl2)
print('VALOR A PAGAR: R$ {:.2f}'.format(total))
