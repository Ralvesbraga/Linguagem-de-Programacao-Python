n1, n2, n3, n4 = input().split()
n1 = float(n1)
n2 = float(n2)
n3 = float(n3)
n4 = float(n4)
media = (n1 * 2 + n2 * 3 + n3 * 4 + n4 * 1)/10
if media >= 7.0:
    print('Media: {:.1f}'.format(media))
    print('Aluno aprovado.')
elif media < 5.0:
    print('Media: {:.1f}'.format(media))
    print('Aluno reprovado.')
else:
    ex = float(input())
    print('Media: {:.1f}'.format(media))
    print('Aluno em exame.')
    media = (media + ex) / 2
    print('Nota do exame: {:.1f}'.format(ex))
    if media >= 5.0:
        print('Aluno aprovado.')
        print('Media final: {:.1f}'.format(media))
    else:
        print('Aluno reprovado.')
        print('Media final: {:.1f}'.format(ex))
