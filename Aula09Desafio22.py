from emoji import emojize
text = emojize(' Desafio 22 :cold_face: ')
print(f'{text:=^30}')

nome = input('\033[33mDigite seu nome completo: ')
maiusculo = nome.upper()
minusculo = nome.lower()
letras = (nome.split())
junto = len(nome.replace(' ',''))
prim_nome = nome.split()[0]
count = len(prim_nome)
print(f'\033[34mSeu nome:\nEm maiúsculo: {maiusculo}\nEm minúsculo: {minusculo}\nLetras ao todo (Sem Espaços): {junto}\nLetras do primeiro nome ({prim_nome}): {count}')
