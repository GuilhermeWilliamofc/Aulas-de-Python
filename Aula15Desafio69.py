from emoji import emojize
text = emojize(' Desafio 69 :moai: ')
print(f'{text:=^30}')

resposta = ' '
contagem = 1
maior = homem = mulheres = 0

while True:
    idade = int(input(f'Digite a Idade da {contagem}º Pessoa: '))
    if idade >= 18:
        maior += 1
    sexo = ' '
    while sexo not in 'mf':
        sexo = input(f'Digite o Sexo da {contagem}º Pessoa [M/F]: ').lower().strip()[0]
    if sexo == 'm':
        homem += 1
    elif sexo == 'f' and idade < 20:
        mulheres += 1
    resposta = input('Deseja Continuar? [S/N]: ').lower().strip()[0]
    while resposta not in 'sn':
        resposta = input('Deseja Continuar? [S/N]: ').lower().strip()[0]
    if resposta == 'n':
        break
    contagem += 1

print(f'Durante a Execução do Programa:\n{maior} Pessoas tem mais de 18 anos\n{homem} Homens Foram Cadastrados\n{mulheres} Mulheres Tem Menos de 20 Anos')
