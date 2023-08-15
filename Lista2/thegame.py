hi, mi, hf, mf = input().split()
hi = int(hi)
mi = int(mi)
hf = int(hf)
mf = int(mf)
horas = 0
if hi == hf and mi == mf:
    print('O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)')
elif hi == hf and mi > mf:
    totmin = 60 + (mf - mi)
    print('O JOGO DUROU 23 HORA(S) E {} MINUTO(S)'.format(totmin))
elif hi > hf:
    totmin = 1440 - ((hi * 60) + mi) + ((hf * 60) + mf)
    horas = totmin // 60
    totmin = totmin % 60
    print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(horas, totmin))
else:
    totmin = ((hf * 60) + mf) - ((hi * 60) + mi)
    if totmin > 59:
        horas = totmin // 60
        totmin = totmin % 60
        print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(horas, totmin))
    else:
        print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(horas, totmin))
