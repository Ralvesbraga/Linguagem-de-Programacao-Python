joias = []
while True:
    try:
        joias.append(input())
    except EOFError:
        print(len(set(joias)))
        break
