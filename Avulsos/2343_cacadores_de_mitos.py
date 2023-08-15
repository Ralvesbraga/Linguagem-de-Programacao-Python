n = int(input())
quad = []
result = 0
a = ''
for i in range(n):
    a = input().strip()
    if a in quad:
        result += 1
    else:
        quad.append(a)
print(result)
