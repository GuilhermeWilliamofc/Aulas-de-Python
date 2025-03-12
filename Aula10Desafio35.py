from emoji import emojize
text = emojize(' Desafio 35 :cold_face: ')
print(f'{text:=^30}')

comprimento1 = float(input('Digite o Primeiro Comprimento: '))
comprimento2 = float(input('Digite o Segundo Comprimento: '))
comprimento3 = float(input('Digite o Terceiro Comprimento: '))

if comprimento1+comprimento2 > comprimento3 and comprimento2+comprimento3 > comprimento1 and comprimento1+comprimento3 > comprimento2:
    print(f'Com esses comprimentos é possível formar um triângulo')
else:
    print(f'Com esses comprimentos não é possível formar um triângulo')
