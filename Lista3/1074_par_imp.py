n = int(input())
for i in range(1, n + 1):
    x = int(input())
    if x > 0:
        if x % 2 == 0:
            print('EVEN POSITIVE')
        else:
            print('ODD POSITIVE')
    elif x == 0:
        print('NULL')
    else:
        if x % 2 == 0:
            print('EVEN NEGATIVE')
        else:
            print('ODD NEGATIVE')
