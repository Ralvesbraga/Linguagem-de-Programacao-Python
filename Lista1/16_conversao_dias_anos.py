dias = int(input())
meses = 0
ano = dias // 365
dias = dias % 365
if dias >= 30:
    meses = dias // 30
    dias = dias % 30
print('{} ano(s)'.format(ano))
print('{} mes(es)'.format(meses))
print('{} dia(s)'.format(dias))
