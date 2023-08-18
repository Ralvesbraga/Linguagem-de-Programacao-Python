n = int(input())
carneiros = list(map(int, input().split()))
i = 0
cont = 0
while 0 <= i < n:
    if cont < i:
        cont = i
    if carneiros[i] % 2 == 0:
        if carneiros[i] == 0:
            i -= 1
        else:
            carneiros[i] -= 1
            i -= 1
    else:
        carneiros[i] -= 1
        i += 1
print(f'{cont+1} {sum(carneiros)}')
