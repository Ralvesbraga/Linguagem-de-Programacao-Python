sal = float(input())
if 0 < sal <= 400:
    reaj = sal
    sal = sal*1.15
    reaj = sal - reaj
    print('Novo salario: {:.2f}'.format(sal))
    print('Reajuste ganho: {:.2f}'.format(reaj))
    print('Em percentual: 15 %')
elif 400 < sal <= 800:
    reaj = sal
    sal = sal * 1.12
    reaj = sal - reaj
    print('Novo salario: {:.2f}'.format(sal))
    print('Reajuste ganho: {:.2f}'.format(reaj))
    print('Em percentual: 12 %')
elif 800 < sal <= 1200:
    reaj = sal
    sal = sal * 1.1
    reaj = sal - reaj
    print('Novo salario: {:.2f}'.format(sal))
    print('Reajuste ganho: {:.2f}'.format(reaj))
    print('Em percentual: 10 %')
elif 1200 < sal <= 2000:
    reaj = sal
    sal = sal * 1.07
    reaj = sal - reaj
    print('Novo salario: {:.2f}'.format(sal))
    print('Reajuste ganho: {:.2f}'.format(reaj))
    print('Em percentual: 7 %')
else:
    reaj = sal
    sal = sal * 1.04
    reaj = sal - reaj
    print('Novo salario: {:.2f}'.format(sal))
    print('Reajuste ganho: {:.2f}'.format(reaj))
    print('Em percentual: 4 %')
