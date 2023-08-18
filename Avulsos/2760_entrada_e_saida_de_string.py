a = input()
b = input()
c = input()
for i in range(3):
    if i == 0:
        print(a+b+c)
    if i == 1:
        print(b+c+a)
    if i == 2:
        print(c+a+b)
print(a[:10]+b[:10]+c[:10])
