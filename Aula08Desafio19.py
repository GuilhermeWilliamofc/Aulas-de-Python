from emoji import emojize
text = emojize('Desafio 19 :cold_face:')
print(f'{text:=^30}')

from random import choice
nome1 = input('Digite o Nome do Aluno 1: ')
nome2 = input('Digite o Nome do Aluno 2: ')
nome3 = input('Digite o Nome do Aluno 3: ')
nome4 = input('Digite o Nome do Aluno 4: ')
nomes = (f'{nome1}',f'{nome2}',f'{nome3}',f'{nome4}')

nomefinal = choice(nomes)
print(nomefinal)
