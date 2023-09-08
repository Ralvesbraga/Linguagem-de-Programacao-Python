n = int(input())
for i in range(n):
    entrada = input()
    p = 0
    c = 0
    s = 0
    for j in entrada:
        if p
        if j == '(':
            p += 1
        elif j == ')':
            p -= 1
            if p < 0:
                break
        if j == '[':
            c += 1
        elif j == ']':
            c -= 1
            if c < 0:
                break
        if j == '{':
            s += 1
        elif j == '}':
            s -= 1
            if s < 0:
                break
    if p == c == s == 0:
        print('S')
    else:
        print('N')
