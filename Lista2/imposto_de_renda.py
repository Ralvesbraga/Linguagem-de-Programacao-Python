sal = float(input())
imposto = 0
if 0 < sal <= 2000:
    print('Isento')
elif 2000 < sal <= 3000:
    imposto = (sal - 2000) * 0.08
    print('R$ {:.2f}'.format(imposto))
elif 3000 < sal <= 4500:
    sal = sal - 3000
    imposto = 1000 * 0.08 + sal * 0.18
    print('R$ {:.2f}'.format(imposto))
elif sal > 4500:
    sal = sal - 4500
    imposto = 1000 * 0.08 + 1500 * 0.18 + sal * 0.28
    print('R$ {:.2f}'.format(imposto))
