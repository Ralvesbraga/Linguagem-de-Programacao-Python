p1, c1, p2, c2 = input().split(' ')
p1 = int(p1)
p2 = int(p2)
c1 = int(c1)
c2 = int(c2)
a = p1 * c1
b = p2 * c2
if a == b:
    print(0)
elif a > b:
    print(-1)
else:
    print(1)
