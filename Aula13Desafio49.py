from emoji import emojize
text = emojize(' Desafio 49 :cold_face: ')
print(f'{text:=^30}')

num = int(input('Digite um número: '))
for tabuada in range(1, 10 + 1):
    conta = num * tabuada
    print(f'{num} x {tabuada} = {conta}')
