cod, qnt = input().split()
cod = int(cod)
qnt = int(qnt)
cq = 4.00
xs = 4.50
xb = 5.00
ts = 2.00
r = 1.50
if cod == 1:
    print('Total: R$ {:.2f}'.format(cq*qnt))
elif cod == 2:
    print('Total: R$ {:.2f}'.format(xs * qnt))
elif cod == 3:
    print('Total: R$ {:.2f}'.format(xb * qnt))
elif cod == 4:
    print('Total: R$ {:.2f}'.format(ts * qnt))
elif cod == 5:
    print('Total: R$ {:.2f}'.format(r * qnt))
