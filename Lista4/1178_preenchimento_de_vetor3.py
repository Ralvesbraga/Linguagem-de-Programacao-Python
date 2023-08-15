x = [float(input())]
for i in range(100):
    x.append(x[i]/2)
    print('N[{}] = {:.4f}'.format(i, x[i]))
