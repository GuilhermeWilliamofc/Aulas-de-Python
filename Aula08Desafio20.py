from emoji import emojize
text = emojize('Desafio 20 :cold_face:')
print(f'{text:=^30}')

from random import sample
aluno1 = input('\033[33mDigite o Nome do Aluno 1: ')
aluno2 = input('Digite o Nome do Aluno 2: ')
aluno3 = input('Digite o Nome do Aluno 3: ')
aluno4 = input('Digite o Nome do Aluno 4: ')
seqalunos = aluno1,aluno2,aluno3,aluno4

print(f'\033[35mA Ordem de Apresentação é:\n{sample(seqalunos, 4)}')

# poderia utilizar a função shuffle do módulo random, não faço ideia de como sample deu certo
