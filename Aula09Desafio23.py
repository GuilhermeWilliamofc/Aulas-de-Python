from emoji import emojize
text = emojize(' Desafio 23 :cold_face: ')
print(f'{text:=^30}')

numero = int((input('\033[35mDigite um número entre 0 e 9999: ')))
u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10
unidade = u
dezena = d
centena = c
milhar = m

print(f'\033[33mO Número {numero} tem:\nUnidade: {unidade}\nDezena: {dezena}\nCentena: {centena}\nMilhar: {milhar}')
