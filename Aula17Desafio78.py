from emoji import emojize
text = emojize(' Desafio 78 :cold_face:')
print(f'{text:=^30}')

num = []
for i in range(1, 6):
    num.append(int(input(f'\033[33mDigite o {i}º Número: ')))

maior = max(num)
menor = min(num)

print(f'\033[32mVocê digitou os valores: {num}')
print(f'O maior valor digitado foi {maior} nas posições: ', end= '')
for i, v in enumerate(num):
    if v == maior:
        print(f'{i}...', end= ' ')

print(f'\nO menor valor digitado foi {menor} nas posições: ', end= '')
for i, v in enumerate(num):
    if v == menor:
        print(f'{i}...', end=' ')
