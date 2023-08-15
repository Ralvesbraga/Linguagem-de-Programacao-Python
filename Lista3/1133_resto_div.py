x = int(input())
y = int(input())
if x > y:
    for y in range(y+1, x):
        if (y % 5 == 2) or (y % 5 == 3):
            print(y)
elif y > x:
    for x in range(x + 1, y):
        if (x % 5 == 2) or (x % 5 == 3):
            print(x)
