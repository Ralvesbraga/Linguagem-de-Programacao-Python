a, c, x, y = input().split()
a = int(a)
c = int(c)
x = int(x)
y = int(y)
totcomp = c - x - y - 1
if totcomp >= a:
    print('Igor feliz!')
else:
    if x > y/2:
        print('Caio, a culpa eh sua!')
    else:
        print('Igor bolado!')
