from math import sqrt
while True:
    try:
        n = int(input())
        for i in range(n + 1):
            if i**2 > n:
                print('NO')
                break
            a = sqrt(n - (i**2))
            if a == int(a):
                b = sqrt(n - (a*a))
                if (a*a)+(b*b) == n:
                    print('YES')
                    break
    except EOFError:
        break
