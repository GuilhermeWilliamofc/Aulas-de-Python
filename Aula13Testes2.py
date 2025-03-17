from emoji import emojize
text = emojize(' Aula 13 - Testes 2 :cold_face: ')
print(f'{text:=^30}')

num = int(input('Digite um número: '))
for c in range(1, num + 1):
    print(c)
print('Fim da Contagem')
