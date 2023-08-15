n = int(input())
v = [0] * 10
for i in range(0, 10):
    if i == 0:
        v[0] = n
    else:
        v[i] = v[i-1] * 2
    print(f'N[{i}] = {v[i]}')
