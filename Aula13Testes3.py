primeiro_num = int(input('Início: '))
ultimo_num = int(input('Fim: '))
de_quanto_em_quanto = int(input('Passo: '))
for c in range(primeiro_num, ultimo_num + 1, de_quanto_em_quanto):
    print(c)
print('Fim da Contagem')
