from emoji import emojize
text = emojize(' Desafio 51 :cold_face: ')
print(f'{text:=^30}')

termo = int(input('Digite o Primeiro Termo: '))
razao = int(input('Digite a Razão: '))
x = 0
for i in range(termo, termo + 10 * razao, razao):
    x += 1
    print(f'O {x}º Termo é {i}')
