n = int(input())
for i in range(n):
    x, y = input().split()
    x = int(x)
    y = int(y)
    if x != 0 and y == 0:
        print('divisao impossivel')
    else:
        print(f'{x/y :.1f}')
    