d, diai = input().split()
horai, minsi, segi = input().split(':')
d2, diaf = input().split()
horaf, minsf, segf = input().split(':')
diai = int(diai)
diaf = int(diaf)
horai = int(horai)
horaf = int(horaf)
minsi = int(minsi)
minsf = int(minsf)
segi = int(segi)
segf = int(segf)
horas = 0
mins = 0
segs = 0
dias = (diaf - diai)
if segi <= segf:
    segs = segf - segi
else:
    segs = 60 + (segf - segi)
    minsf = minsf - 1
if minsi <= minsf:
    mins = minsf - minsi
else:
    mins = 60 + (minsf - minsi)
    horaf = horaf - 1
if horai <= horaf:
    horas = (horaf - horai)
elif horai > horaf:
    horas = 24 + horaf - horai
    dias = dias - 1
print('{} dia(s)'.format(dias))
print('{} hora(s)'.format(horas))
print('{} minuto(s)'.format(mins))
print('{} segundo(s)'.format(segs))
