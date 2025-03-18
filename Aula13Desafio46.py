from emoji import emojize
from time import sleep
text = emojize(' Desafio 46 :cold_face: ')
print(f'{text:=^30}')

print('\033[31mContagem Regressiva Ano Novo!')
for c in range (10, -1, -1):
    print(c)
    sleep(1)
print('\033[32mFeliz Ano Novo!')
