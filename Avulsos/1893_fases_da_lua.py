i, f = map(int, input().split())
if i < f:
    if 0 <= f <= 2:
        print('nova')
    elif 3 <= f <= 96:
        print('crescente')
    else:
        print('cheia')
elif i >= f:
    if 2 >= f >= 0:
        print('nova')
    elif 96 >= f >= 3:
        print('minguante')
    else:
        print('cheia')
