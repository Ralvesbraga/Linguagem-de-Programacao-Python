n = int(input())
for i in range(n):
    pal = ''
    pal1,pal2 = input().split()
    pal3 = ''
    if len(pal1) >= len(pal2):
        menor = len(pal2)
        pal3 = pal1
    else:
        menor = len(pal1)
        pal3 = pal2
    for j in range(menor):
        pal += pal1[j] + pal2[j]
    print(pal+pal3[menor:])
