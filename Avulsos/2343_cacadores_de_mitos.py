n = int(input())
quad = []
a = ''
for i in range(n):
    a = input().strip()
    quad.append(a)
squad = set(quad)
if len(quad) == len(squad):
    print(0)
else:
    print(1)
