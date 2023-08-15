n = int(input())
pavs = input().split()
for i in range(len(pavs)):
    if len(pavs[i]) == 3:
        a = list(pavs[i])
        b = pavs[i]
        if b[0:2] == 'OB' or b[0:2] == 'UR':
            a.pop(2)
            a.append('I')
            pavs.pop(i)
            pavs.insert(i, ''.join(a))
print(*pavs)