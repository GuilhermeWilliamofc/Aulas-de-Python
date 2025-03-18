from emoji import emojize
text = emojize(' Desafio 56 :cold_face: ')
print(f'{text:=^30}')

media = 0
velho = 0
sexo_fem = 0
nome_velho = ''
for i in range(1, 5):
    nome = input(f'Digite o nome da {i}º pessoa: ').strip()
    idade = int(input(f'Digite a Idade da {i}º pessoa: '))
    sexo = int(input(f'Qual o Sexo?\n[ 1 ] - Masculino\n[ 2 ] - Feminino\nDigite o Sexo: '))
    media += idade
    if i == 1 and sexo == 1:
        velho = idade
        nome_velho = nome
    else:
        if idade > velho and sexo == 1:
            nome_velho = nome
            velho = idade
        if idade < 20 and sexo == 2:
            sexo_fem += 1

media_idade = media / 4
print(f'A Média de Idade do Grupo é de {media_idade:.2f}\nO Nome do Homem Mais Velho é {nome_velho} e tem {velho} Anos\n{sexo_fem} Mulher(es) tem menos de 20 Anos')
