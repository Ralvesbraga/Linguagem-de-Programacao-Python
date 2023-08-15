n = int(input())
for i in range(n):
    palavra = list(input())
    asci = []
    for j in palavra:
        if j == ' ':
            asci.append(j)
        else:
            if j.isalpha():
                asci.append(chr(ord(j) + 3))
            else:
                asci.append(j)

    asci.reverse()
    for j in range(len(asci)//2, len(asci)):
        asci[j] = chr((ord(asci[j]) - 1))
    asci = ''.join(asci)
    print(asci)
