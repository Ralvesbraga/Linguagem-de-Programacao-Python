media = 0
pos = 0
for i in range(1, 7):
    x = float(input())
    if x > 0:
        pos += 1
        media += x
print(f'{pos} valores positivos')
print('{:.1f}'.format(media/pos))
